
from threading import Lock

class ClipboardManager:
    def __init__(self):
        self._content = ""
        self._lock = Lock()

    def get_content(self):
        with self._lock:
            return self._content

    def set_content(self, content):
        with self._lock:
            self._content = content