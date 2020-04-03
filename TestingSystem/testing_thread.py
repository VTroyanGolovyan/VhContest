from threading import Thread
from testers import *


class TestingThread(Thread):
    def __init__(self, CONFIG, connect):
        Thread.__init__(self)
        self.CONFIG = CONFIG
        self.connect = connect

    def run(self):
        pass
