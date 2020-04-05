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
        sendingID = self.connect.recv(16)
        sendingData = self.getSendingData(sendingID)
        tester = self.createTester('c++')
        tester.runSolutionTesting()

    def getSendingData(self, sendingID):
        return self.CONFIG

    def createTester(self, language):
        global languageSettings
        if languageSettings[language].type == 0:
            return CompilingTester(
                self.CONFIG,
                languageSettings[language],
                1000,
                124,
                1
            )
        elif languageSettings[language].type == 1:
            return InterpretingTester(
                self.CONFIG,
                languageSettings[language],
                1000,
                124,
                1
            )
        elif languageSettings[language].type == 0:
            return SomeAverageTester(
                self.CONFIG,
                languageSettings[language],
                1000,
                124,
                1
            )
