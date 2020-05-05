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
        self.t = 0

    def run(self):
        try:
            while True:
                print(self.util.cpu_times())
                self.rss = max(self.rss, self.util.memory_info().rss)
                times = self.util.cpu_times()
                self.cpu = times.user + times.system + times.children_system + times.children_user
                self.t += 0.05
                if self.cpu == 0:
                    self.cpu = self.t
                time.sleep(0.05)
        except Exception:
            return
