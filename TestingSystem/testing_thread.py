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
        sendingArray = sending.split(' ')
        sendingId = sendingArray[2]
        userId = sendingArray[1]
        sendingData = self.getSendingData(sendingId)

        tester = self.createTester('python')
        testingPath = self.CONFIG['TestingDirectory'] + '1/'
        sourceFile = testingPath + 'main.py'

        f = open(sourceFile, 'w')
        f.write(sendingData[4])
        f.close()
        res = 'OK'

        timeout, memLimit = self.getLimits(sendingData[3])
        maxTime = 0
        maxMem = 0
        for test in self.getTests(sendingData[3]):
            res = tester.runSolutionTesting(testingPath, sourceFile, test, timeout, memLimit)
            maxTime = max(maxTime, res[2])
            maxMem = max(maxMem, res[1])
            if res[0] != 'OK':
                break
        self.saveResults(sendingId, res, maxTime * 1000, maxMem)
        self.db.close()

    def getSendingData(self, sendingId):
        with self.db as db:
            db.execute("SELECT * FROM `sendings` WHERE `id`={0}".format(sendingId))
            rows = db.fetchall()
            return rows[0]

    def saveResults(self, sendingId, result, maxTime, maxMem):
        with self.db as db:
            db.execute(
                "UPDATE `sendings` SET `result`='{1}', `time`='{2}', `memory`='{3}'  WHERE `id`={0}".format(
                    sendingId,
                    result[0],
                    maxTime,
                    maxMem
                )
            )
        self.db.commit()

    def getTests(self, taskId):
        with self.db as db:
            db.execute("SELECT * FROM `tests` WHERE `task_id`={0}".format(taskId))
            return db.fetchall()

    def getLimits(self, taskId):
        with self.db as db:
            db.execute("SELECT * FROM `tasks` WHERE `id`={0}".format(taskId))
            res = db.fetchall()[0]

            return int(res[3]) // 1000, int(res[4])

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
