from threading import Thread
from testers import *
import pymysql
import subprocess
import os


class TestingThread(Thread):
    def __init__(self, CONFIG, connect):
        Thread.__init__(self)
        self.CONFIG = CONFIG
        self.connect = connect
        self.db = pymysql.connect(
            host=self.CONFIG['DBHost'],
            db=self.CONFIG['DBName'],
            user=self.CONFIG['DBUser'],
            password=self.CONFIG['DBPassword'],
            charset='utf8'
        )

    def run(self):
        languageSettings = self.CONFIG['languages']
        sending = self.connect.recv(256).decode('utf-8')
        sendingArray = sending.split(' ')
        sendingId = sendingArray[2]
        userId = sendingArray[1]

        sendingData = self.getSendingData(sendingId)

        language = sendingData['language']

        testingPath = self.CONFIG['TestingDirectory'] + str(sendingId) + '/'
        os.mkdir(testingPath)
        sourceFile = testingPath + 'Main.' + languageSettings[language].fileEnd

        f = open(sourceFile, 'w')
        f.write(sendingData['code'])
        f.close()

        if languageSettings[language].runningType in [0, 2]:

            process = subprocess.Popen(
                languageSettings[language].compilerBash.format(testingPath, sourceFile),
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True,
                executable='/bin/bash'
            )
            output, error = process.communicate()
            if error.decode('utf-8') != '':
                self.saveResults(sendingId, 'CE', 0, 0)
                self.db.close()
                return

        res = 'OK'

        timeout, memLimit = self.getLimits(sendingData['task_id'])
        maxTime = 0
        maxMem = 0
        tester = self.createTester(language)
        for test in self.getTests(sendingData['task_id']):
            res = tester.runSolutionTesting(testingPath, sourceFile, test, timeout, memLimit)
            maxTime = max(maxTime, res[2])
            maxMem = max(maxMem, res[1])
            if res[0] != 'OK':
                break
        self.saveResults(sendingId, res, maxTime * 1000, maxMem)
        self.db.close()

    def getSendingData(self, sendingId):
        with self.db.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("SELECT * FROM `sendings` WHERE `id`={0}".format(sendingId))
            rows = cursor.fetchall()
            return rows[0]

    def saveResults(self, sendingId, result, maxTime, maxMem):
        with self.db.cursor() as cursor:
            cursor.execute(
                "UPDATE `sendings` SET `result`='{1}', `time`='{2}', `memory`='{3}'  WHERE `id`={0}".format(
                    sendingId,
                    result[0],
                    maxTime,
                    maxMem
                )
            )
        self.db.commit()

    def getTests(self, taskId):
        with self.db.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("SELECT * FROM `tests` WHERE `task_id`={0}".format(taskId))
            return cursor.fetchall()

    def getLimits(self, taskId):
        with self.db as db:
            db.execute("SELECT `time_limit`, `memory_limit` FROM `tasks` WHERE `id`={0}".format(taskId))
            res = db.fetchall()[0]
            return int(res[0]) // 1000, int(res[1])

    def createTester(self, language):
        languageSettings = self.CONFIG['languages']
        if languageSettings[language].runningType == 0:
            return CompilingTester(
                self.CONFIG,
                languageSettings[language]
            )
        elif languageSettings[language].runningType == 1:
            return InterpretingTester(
                self.CONFIG,
                languageSettings[language]
            )
        elif languageSettings[language].runningType == 2:
            return SomeAverageTester(
                self.CONFIG,
                languageSettings[language]
            )
