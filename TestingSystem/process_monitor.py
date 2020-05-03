from threading import Thread
import psutil
import time


class ProccesMonitor(Thread):
    def __init__(self, proc):
        super().__init__()
        self.CPU = 0
        self.time = 0
        self.proc = proc

    def run(self):
        time.sleep(0.05)
