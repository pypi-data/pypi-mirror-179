"""Null preview"""

from logging import getLogger
import threading


_log = getLogger(__name__)


class NullPreview:
    """Null Preview"""

    def thread_func(self, picam2):
        """Thread function

        :param picam2: picamera2 object
        :type picam2: Picamera2
        """
        import selectors

        sel = selectors.DefaultSelector()
        sel.register(picam2.notifyme_r, selectors.EVENT_READ, self.handle_request)
        self._started.set()

        while not self._abort.is_set():
            events = sel.select(0.2)
            for key, _ in events:
                picam2.notifymeread.read()
                callback = key.data
                callback(picam2)

    def __init__(self, x=None, y=None, width=None, height=None, transform=None):
        """Initialise null preview

        :param x: X position, defaults to None
        :type x: int, optional
        :param y: Y position, defaults to None
        :type y: int, optional
        :param width: Width, defaults to None
        :type width: int, optional
        :param height: Height, defaults to None
        :type height: int, optional
        :param transform: Transform, defaults to None
        :type transform: libcamera.Transform, optional
        """
        # Ignore width and height as they are meaningless. We only accept them so as to
        # be a drop-in replacement for the Qt/DRM previews.
        self.size = (width, height)
        self._abort = threading.Event()
        self._started = threading.Event()
        self.picam2 = None

    def start(self, picam2):
        """Starts null preview

        :param picam2: Picamera2 object
        :type picam2: Picamera2
        """
        self.picam2 = picam2
        self._started.clear()
        self._abort.clear()
        self.thread = threading.Thread(target=self.thread_func, args=(picam2,))
        self.thread.setDaemon(True)
        self.thread.start()
        self._started.wait()

    def set_overlay(self, overlay):
        """Sets overlay

        :param overlay: Overlay
        """
        # This only exists so as to have the same interface as other preview windows.
        pass

    def handle_request(self, picam2):
        """Handle requests

        :param picam2: picamera2 object
        :type picam2: Picamera2
        """
        try:
            completed_request = picam2.process_requests()
        except Exception as e:
            _log.exception("Exception during process_requests()", exc_info=e)
            raise

        if completed_request:
            completed_request.release()

    def stop(self):
        """Stop preview"""
        self._abort.set()
        self.thread.join()
        self.picam2 = None

    def set_title_function(self, function):
        pass
