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
        self.sourceName = ''

    def runSolutionTesting(self):
        pass

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
            self.CONFIG['TestingDirectory'],
            self.sourceName,
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
            self.CONFIG['TestingDirectory'],
            self.sourceName,
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
            self.CONFIG['TestingDirectory'],
            self.sourceName,
            self.timeLimit,
            self.memoryLimit,
            self.processLimit
        )
