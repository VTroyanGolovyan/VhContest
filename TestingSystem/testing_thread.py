from threading import Thread
from runners import RunningSettings
from testers import *

languageSettings = dict(
    [
        (
            'c++',
            RunningSettings(
                0,
                'g++ {0} -o Main',
                '',
                ''
            )
        ),
    ]
)


class TestingThread(Thread):
    def __init__(self, CONFIG, connect):
        Thread.__init__(self)
        self.CONFIG = CONFIG
        self.connect = connect

    def run(self):
        pass
