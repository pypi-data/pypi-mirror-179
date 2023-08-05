# cython: language_level=3
# distutils: language = c++

from libc.math cimport lround


cdef class Sender:
    """Sends video and audio streams


    Attributes:
        ndi_name (str): The |NDI| source name to use
        ndi_source (Source): A source object representing the sender
        video_frame (VideoSendFrame):
        audio_frame (AudioSendFrame):
        metadata_frame (MetadataSendFrame):
        num_video_buffers (int): Number of video frames to allocate as buffers
        num_audio_buffers (int): Number of audio frames to allocate as buffers
        clock_video (bool): True if the video frames should clock themselves.
            If False, no rate limiting will be applied to keep within the
            desired frame rate
        clock_audio (bool): True if the audio frames should clock themselves.
            If False, no rate limiting will be applied to keep within the
            desired frame rate

    """
    def __cinit__(self, *args, **kwargs):
        self.ptr = NULL
        self.source_ptr = NULL
        self.has_video_frame = False
        self.has_audio_frame = False
        # self.has_metadata_frame = False
        self.video_frame = None
        self.audio_frame = None
        # self.metadata_frame = None

    def __init__(
        self,
        str ndi_name,
        str ndi_groups='',
        bint clock_video=True,
        bint clock_audio=True,
        size_t num_video_buffers=2,
        size_t num_audio_buffers=2,
    ):
        self.num_video_buffers = num_video_buffers
        self.num_audio_buffers = num_audio_buffers
        self.ndi_name = ndi_name
        self.ndi_groups = ndi_groups
        self._b_ndi_name = ndi_name.encode()
        self._b_ndi_groups = ndi_groups.encode()
        self.clock_video = clock_video
        self.clock_audio = clock_audio
        self.metadata_frame = MetadataSendFrame('')
        self.source = None
        send_t_initialize(&(self.send_create), self._b_ndi_name, NULL)
        if len(self._b_ndi_groups):
            self.send_create.ndi_groups = self._b_ndi_groups


    def __dealloc__(self):
        cdef NDIlib_send_instance_t ptr = self.ptr
        self.ptr = NULL
        if ptr is not NULL:
            NDIlib_send_destroy(ptr)

    @property
    def name(self):
        """The current name of the source

        This may be different than what was supplied during initialization
        """
        if self.source is not None:
            return self.source.name
        return self.ndi_name

    @property
    def program_tally(self):
        """The current program tally state of the sender
        """
        if self.source is not None:
            return self.source.tally.on_program
        return False

    @property
    def preview_tally(self):
        """The current preview tally state of the sender
        """
        if self.source is not None:
            return self.source.tally.on_preview
        return False

    @property
    def has_any_frame(self):
        return self.has_video_frame or self.has_audio_frame

    def open(self):
        """Open the sender
        """
        self._open()

    def close(self):
        """Close the sender and free all resources
        """
        self._close()

    def __enter__(self):
        self._open()
        return self

    def __exit__(self, *args):
        self._close()

    cdef void _open(self) except *:
        if self._running:
            return
        if not self.has_video_frame and not self.has_audio_frame:
            raise_exception('Cannot start sender. No frame objects')
        self._running = True
        cdef NDIlib_send_instance_t ptr
        cdef void* source_ptr
        try:
            if self.has_video_frame:
                self.video_frame._create_child_frames(self.num_video_buffers - 1)
                self.video_frame._set_sender_status(True)
            if self.has_audio_frame:
                self.audio_frame._create_child_frames(self.num_audio_buffers - 1)
                self.audio_frame._set_sender_status(True)
            self.send_create.clock_video = self.clock_video
            self.send_create.clock_audio = self.clock_audio
            self.ptr = NDIlib_send_create(&(self.send_create))
            if self.ptr is NULL:
                raise_mem_err()

            # Cast from void* to avoid clang "const" compile errors
            source_ptr = <void*>NDIlib_send_get_source_name(self.ptr)
            self.source_ptr = <NDIlib_source_t*>source_ptr
            assert self.source_ptr is not NULL
            self.source = Source.create_no_parent(self.source_ptr)
        except Exception as exc:
            print('caught exc: ', exc)
            self._running = False
            ptr = self.ptr
            self.ptr = NULL
            if ptr is not NULL:
                NDIlib_send_destroy(ptr)
            self.video_frame._destroy()
            self.video_frame._set_sender_status(False)
            self.audio_frame._destroy()
            self.audio_frame._set_sender_status(False)
            raise

    cdef void _close(self) except *:
        if not self._running:
            return
        self._running = False
        cdef NDIlib_send_instance_t ptr = self.ptr
        self.ptr = NULL
        if ptr is not NULL:
            NDIlib_send_destroy(ptr)
        if self.has_video_frame:
            self.video_frame._destroy()
            self.video_frame._set_sender_status(False)
        if self.has_audio_frame:
            self.audio_frame._destroy()
            self.audio_frame._set_sender_status(False)

    cpdef set_video_frame(self, VideoSendFrame vf):
        """Set the :attr:`video_frame`
        """
        if self._running:
            raise Exception('Cannot add frame while sender is open')
        self.video_frame = vf
        self.has_video_frame = vf is not None

    cpdef set_audio_frame(self, AudioSendFrame af):
        """Set the :attr:`audio_frame`
        """
        if self._running:
            raise Exception('Cannot add frame while sender is open')
        self.audio_frame = af
        self.has_audio_frame = af is not None

    cdef void _check_running(self) nogil except *:
        if not self._running:
            raise_exception('Not running')
        if self.ptr is NULL:
            raise_exception('ptr is NULL')

    def write_video_and_audio(self, cnp.uint8_t[:] video_data, cnp.float32_t[:,:] audio_data):
        """Write and send the given video and audio data

        The video data will be sent asynchronously (as described in
        :meth:`write_video_async`).

        Arguments:
            video_data: A 1-d array or memoryview of unsigned 8-bit integers
                formatted as described in :class:`.wrapper.FourCCPackInfo`
            audio_data: A 2-d array or memoryview of 32-bit floats with shape
                ``(num_channels, num_samples)``

        """
        return self._write_video_and_audio(video_data, audio_data)

    cdef bint _write_video_and_audio(
        self,
        cnp.uint8_t[:] video_data,
        cnp.float32_t[:,:] audio_data,
    ) except *:
        self._check_running()
        cdef VideoSendFrame_status* vid_send_status
        cdef NDIlib_video_frame_v2_t* vid_ptr
        cdef AudioSendFrame_status* aud_send_status
        cdef NDIlib_audio_frame_v3_t* aud_ptr
        cdef bint vid_result = True, aud_result = True

        vid_send_status = self.video_frame._get_next_write_frame()
        aud_send_status = self.audio_frame._get_next_write_frame()
        cdef cnp.uint8_t[:] vid_memview = self.video_frame
        cdef cnp.float32_t[:,:] aud_memview = self.audio_frame

        vid_result = vid_send_status is not NULL
        aud_result = aud_send_status is not NULL
        if not vid_result or not aud_result:
            raise_exception('send_status is NULL')

        with nogil:
            self.audio_frame._set_shape_from_memview(aud_send_status, audio_data)
            aud_memview[:aud_send_status.shape[0],:aud_send_status.shape[1]] = audio_data
            self.audio_frame._set_buffer_write_complete(aud_send_status)

            vid_memview[...] = video_data
            self.video_frame._set_buffer_write_complete(vid_send_status)

            vid_ptr = vid_send_status.frame_ptr[0]
            aud_ptr = aud_send_status.frame_ptr[0]
            NDIlib_send_send_video_async_v2(self.ptr, vid_ptr)
            self.video_frame._on_sender_write(vid_send_status)
            NDIlib_send_send_audio_v3(self.ptr, aud_ptr)
            self.audio_frame._on_sender_write(aud_send_status)

        return vid_result and aud_result

    def write_video(self, cnp.uint8_t[:] data):
        """Write the given video data and send it

        Arguments:
            data: A 1-d array or memoryview of unsigned 8-bit integers
                formatted as described in :class:`.wrapper.FourCCPackInfo`
        """
        return self._write_video(data)

    cdef bint _write_video(self, cnp.uint8_t[:] data) except *:
        self._check_running()
        cdef VideoSendFrame_status* send_status = self.video_frame._get_next_write_frame()
        if send_status is NULL:
            raise_exception('send_status is NULL')
        cdef NDIlib_video_frame_v2_t* vid_ptr = send_status.frame_ptr[0]
        cdef cnp.uint8_t[:] vid_memview = self.video_frame

        with nogil:
            vid_memview[...] = data
            self.video_frame._set_buffer_write_complete(send_status)
            NDIlib_send_send_video_v2(self.ptr, vid_ptr)
            self.video_frame._on_sender_write(send_status)
        return True

    def write_video_async(self, cnp.uint8_t[:] data):
        """Write the given video data and send it asynchronously

        This call will return immediately and the required operations on the
        data will be handled separately by the |NDI| library.

        .. note::

            This is not an :keyword:`async def` function

        Arguments:
            data: A 1-d array or memoryview of unsigned 8-bit integers
                formatted as described in :class:`.wrapper.FourCCPackInfo`

        """
        return self._write_video_async(data)

    cdef bint _write_video_async(self, cnp.uint8_t[:] data) except *:
        self._check_running()
        cdef VideoSendFrame_status* send_status = self.video_frame._get_next_write_frame()
        if send_status is NULL:
            raise_exception('send_status is NULL')
        cdef NDIlib_video_frame_v2_t* vid_ptr = send_status.frame_ptr[0]
        cdef cnp.uint8_t[:] vid_memview = self.video_frame

        with nogil:
            vid_memview[...] = data
            self.video_frame._set_buffer_write_complete(send_status)
            NDIlib_send_send_video_async_v2(self.ptr, vid_ptr)
            self.video_frame._on_sender_write(send_status)
        return True

    def send_video(self):
        return self._send_video()

    def send_video_async(self):
        return self._send_video_async()

    cdef bint _send_video(self) except *:
        self._check_running()
        if not self.video_frame._send_frame_available():
            return False
        cdef VideoSendFrame_status* send_status = self.video_frame._get_send_frame()
        cdef NDIlib_video_frame_v2_t* vid_ptr = send_status.frame_ptr[0]
        NDIlib_send_send_video_v2(self.ptr, vid_ptr)
        self.video_frame._on_sender_write(send_status)
        return True

    cdef bint _send_video_async(self) except *:
        self._check_running()
        if not self.video_frame._send_frame_available():
            return False
        cdef VideoSendFrame_status* send_status = self.video_frame._get_send_frame()
        cdef NDIlib_video_frame_v2_t* vid_ptr = send_status.frame_ptr[0]
        NDIlib_send_send_video_async_v2(self.ptr, vid_ptr)
        self.video_frame._on_sender_write(send_status)
        return True

    def write_audio(self, cnp.float32_t[:,:] data):
        """Write the given audio data and send it

        Arguments:
            data: A 2-d array or memoryview of 32-bit floats with shape
                ``(num_channels, num_samples)``
        """
        return self._write_audio(data)

    cdef bint _write_audio(self, cnp.float32_t[:,:] data) except *:
        self._check_running()
        cdef NDIlib_audio_frame_v3_t* aud_ptr
        cdef AudioSendFrame_status* send_status = self.audio_frame._get_next_write_frame()
        cdef cnp.float32_t[:,:] aud_memview = self.audio_frame
        if send_status is NULL:
            raise_exception('send_status is NULL')

        with nogil:
            self.audio_frame._set_shape_from_memview(send_status, data)
            aud_memview[:send_status.shape[0],:send_status.shape[1]] = data
            aud_ptr = send_status.frame_ptr[0]
            NDIlib_send_send_audio_v3(self.ptr, aud_ptr)
            self.audio_frame._on_sender_write(send_status)
        return True

    def send_audio(self):
        return self._send_audio()

    cdef bint _send_audio(self) except *:
        if not self._running:
            return False
        if not self.audio_frame._send_frame_available():
            return False
        cdef AudioSendFrame_status* send_status = self.audio_frame._get_send_frame()
        if send_status is NULL:
            raise_exception('no send pointer')
        assert send_status.id == send_status.next_send_id

        cdef NDIlib_audio_frame_v3_t* aud_ptr = send_status.frame_ptr[0]
        NDIlib_send_send_audio_v3(self.ptr, aud_ptr)
        self.audio_frame._on_sender_write(send_status)
        return True

    def send_metadata(self, str tag, dict attrs):
        return self._send_metadata(tag, attrs)

    cdef bint _send_metadata(self, str tag, dict attrs) except *:
        self.metadata_frame._clear()
        self.metadata_frame.tag = tag
        self.metadata_frame.attrs.update(attrs)
        return self._send_metadata_frame(self.metadata_frame)

    def send_metadata_frame(self, MetadataSendFrame mf):
        return self._send_metadata_frame(mf)

    cdef bint _send_metadata_frame(self, MetadataSendFrame mf) except *:
        if not mf._serialize():
            return False
        NDIlib_send_send_metadata(self.ptr, mf.ptr)
        return True

    def get_num_connections(self, double timeout):
        cdef uint32_t timeout_ms = lround(timeout)
        return self._get_num_connections(timeout_ms)

    cdef int _get_num_connections(self, uint32_t timeout_ms) nogil except *:
        return NDIlib_send_get_no_connections(self.ptr, timeout_ms)

    def update_tally(self, double timeout):
        cdef uint32_t timeout_ms = lround(timeout)
        return self._update_tally(timeout_ms)

    cdef bint _update_tally(self, uint32_t timeout_ms) nogil except *:
        self._check_running()
        cdef NDIlib_tally_t* tally = &(self.source.tally)
        cdef bint pgm = tally.on_program, pvw = tally.on_preview
        NDIlib_send_get_tally(self.ptr, tally, timeout_ms)
        cdef bint changed = pgm is not tally.on_program or pvw is not tally.on_preview
        return changed
