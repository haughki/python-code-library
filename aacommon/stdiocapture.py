import sys
from io import StringIO


class StdOutCapture:
    def __init__(self):
        self._old_stdout = sys.stdout
        sys.stdout = self._capture = StringIO()

    def value(self):
        sys.stdout.flush()
        self._capture.flush()
        return self._capture.getvalue()
    
    def close(self):
        sys.stdout.flush()
        sys.stdout = self._old_stdout
        self._capture.close()


class StdInFromString:
    def __init__(self, str_in):
        self._old_stdin = sys.stdin
        sys.stdin = StringIO(str_in)

    def close(self):
        sys.stdin.close()
        sys.stdin = self._old_stdin