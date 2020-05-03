from runners import CompilerRunner, InterpreterRunner, SomeAverageRunner


class Tester:
    def __init__(
            self,
            CONFIG,
            runningSettings,
            timeLimit,
            memoryLimit,
            processLimit
    ):
        self.CONFIG = CONFIG
        self.runningSettings = runningSettings
        self.timeLimit = timeLimit
        self.memoryLimit = memoryLimit
        self.processLimit = processLimit
        self.runner = self.createRunner()

    def runSolutionTesting(
            self,
            testingPath,
            sourceFile,
            test,
            timout,
            memory
    ):
        result = self.runner.runProgram(
            sourceFile,
            test[2],
            timout,
            memory
        )

        memUsage = result[3] // 1024 // 1024
        timeUsage = result[4]
        if result[2] != 'NL':
            return result[2], memUsage, timeUsage
        if result[0].decode('utf-8').strip() == test[3]:
            return 'OK', memUsage, timeUsage
        else:
            return 'WA', memUsage, timeUsage

    def createRunner(self):
        pass


class CompilingTester(Tester):
    def __init__(
            self,
            CONFIG,
            runningSettings,
            timeLimit,
            memoryLimit,
            processLimit
    ):
        Tester.__init__(
            self,
            CONFIG,
            runningSettings,
            timeLimit,
            memoryLimit,
            processLimit
        )

    def createRunner(self):
        return CompilerRunner(
            self.runningSettings,
            self.CONFIG['ControllerBinPath'],
            self.timeLimit,
            self.memoryLimit,
            self.processLimit
        )


class InterpretingTester(Tester):
    def __init__(
            self,
            CONFIG,
            runningSettings,
            timeLimit,
            memoryLimit,
            processLimit
    ):
        Tester.__init__(
            self,
            CONFIG,
            runningSettings,
            timeLimit,
            memoryLimit,
            processLimit
        )

    def createRunner(self):
        return InterpreterRunner(
            self.runningSettings,
            self.CONFIG['ControllerBinPath'],
            self.timeLimit,
            self.memoryLimit,
            self.processLimit
        )


class SomeAverageTester(Tester):
    def __init__(
            self,
            CONFIG,
            runningSettings,
            timeLimit,
            memoryLimit,
            processLimit
    ):
        Tester.__init__(
            self,
            CONFIG,
            runningSettings,
            timeLimit,
            memoryLimit,
            processLimit
        )

    def createRunner(self):
        return SomeAverageRunner(
            self.runningSettings,
            self.CONFIG['ControllerBinPath'],
            self.timeLimit,
            self.memoryLimit,
            self.processLimit
        )
