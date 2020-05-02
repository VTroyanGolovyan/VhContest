from threading import Thread
from runners import RunningSettings
from testers import *
import pymysql

languageSettings = {

    'c++': RunningSettings(
        0,
        'g++ {0} -o Main',
        '',
        ''
    ),
    'python': RunningSettings(
        1,
        '',
        'python3 {0}',
        ''
    )
}


class TestingThread(Thread):
    def __init__(self, CONFIG, connect):
        Thread.__init__(self)
        self.CONFIG = CONFIG
        self.connect = connect
        self.db = pymysql.connect(
            'localhost',
            'root',
            'root',
            'VHcontest'
        )

    def run(self):
        sending = self.connect.recv(256).decode('utf-8')
        print(sending)
        sendingArray = sending.split(' ')
        sendingId = sendingArray[2]
        userId = sendingArray[1]
        sendingData = self.getSendingData(sendingId)

        tester = self.createTester('python')
        testingPath = self.CONFIG['ControllerBinPath'] + '/TestingDirectory/1/'
        sourceFile = testingPath + 'main.py'
        f = open(sourceFile, 'w')
        f.write(sendingData[4])
        f.close()
        for test in self.getTests(sendingData[1]):
            print(test)
        tester.runSolutionTesting()

    def getSendingData(self, sendingId):
        with self.db as db:

            db.execute("SELECT * FROM `sendings` WHERE `id`={0}".format(sendingId))

            rows = db.fetchall()
            return rows[0]

    def getTests(self, taskId):
        with self.db as db:
            db.execute("SELECT * FROM `tests` WHERE `task_id`={0}".format(sendingID))
            return db.fetchall()


    def createTester(self, language):
        global languageSettings
        if languageSettings[language].runningType == 0:
            return CompilingTester(
                self.CONFIG,
                languageSettings[language],
                1000,
                124,
                1
            )
        elif languageSettings[language].runningType == 1:
            return InterpretingTester(
                self.CONFIG,
                languageSettings[language],
                1000,
                124,
                1
            )
        elif languageSettings[language].runningType == 0:
            return SomeAverageTester(
                self.CONFIG,
                languageSettings[language],
                1000,
                124,
                1
            )
