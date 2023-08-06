import logging
import threading
import time

class TimeoutSwitchingFileHandler(logging.Handler):
    def __init__(self, filename, min_timeout=60, max_timeout=3600):
        super().__init__()
        self.basename = filename
        self.min_timeout = min_timeout
        self.max_timeout = max_timeout
        self.fh = None
        self.last_emit = 0
        self.first_emit = 0
        self.last_emit = 0
        cleanup = threading.Thread(target=self.cleanup_loop, daemon=True)
        cleanup.start()

    def emit(self, record):
        msg = self.format(record)
        now = time.time()
        if not self.fh:
            now_tm = time.localtime(now)
            filename = self.basename + time.strftime("%Y-%m-%d-%H-%M-%S", now_tm) + "-%06d" % (now % 1 * 1000000) + ".log"
            self.fh = open(filename, "a")
            self.first_emit = now
        self.fh.write(msg)
        self.fh.write("\n")
        self.fh.flush()
        self.last_emit = now

    def cleanup_loop(self):
        while True:
            time.sleep(1)
            self.acquire()
            now = time.time()
            if self.fh and now - self.last_emit > self.min_timeout:
                self.fh.close()
                self.fh = None
            if self.fh and now - self.first_emit > self.max_timeout:
                self.fh.close()
                self.fh = None
            self.release()
