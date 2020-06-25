from runners import CompilerRunner, InterpreterRunner, SomeAverageRunner


class Tester:
    def __init__(
            self,
            CONFIG,
            runningSettings
    ):
        self.CONFIG = CONFIG
        self.runningSettings = runningSettings
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
            testingPath,
            sourceFile,
            test['input'],
            timout,
            memory
        )

        memUsage = result[3] // 1024 // 1024
        timeUsage = result[4]
        if result[2] != 'NL':
            return result[2], memUsage, timeUsage
        if result[0].decode('utf-8').strip() == test['output']:
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
    ):
        Tester.__init__(
            self,
            CONFIG,
            runningSettings,
        )

    def createRunner(self):
        return CompilerRunner(
            self.runningSettings
        )


class InterpretingTester(Tester):
    def __init__(
            self,
            CONFIG,
            runningSettings
    ):
        Tester.__init__(
            self,
            CONFIG,
            runningSettings,
        )

    def createRunner(self):
        return InterpreterRunner(
            self.runningSettings
        )


class SomeAverageTester(Tester):
    def __init__(
            self,
            CONFIG,
            runningSettings
    ):
        Tester.__init__(
            self,
            CONFIG,
            runningSettings
        )

    def createRunner(self):
        return SomeAverageRunner(
            self.runningSettings
        )
