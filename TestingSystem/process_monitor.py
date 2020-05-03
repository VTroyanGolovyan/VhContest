from threading import Thread
import psutil
import time


class ProcessMonitor(Thread):
    def __init__(self, proc):
        super().__init__()
        self.rss = 0
        self.cpu = 0
        self.proc = proc
        self.util = psutil.Process(proc.pid)

    def run(self):
        try:
            while True:
                self.rss = max(self.rss, self.util.memory_info().rss)
                self.cpu = self.util.cpu_times().user + self.util.cpu_times().system
                time.sleep(0.05)
        except Exception:
            return
