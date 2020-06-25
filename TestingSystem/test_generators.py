from runners import CompilerRunner, InterpreterRunner, SomeAverageRunner


class TestGenerator:
    def __init__(
            self,
            CONFIG,
            runningSettings
    ):
        self.CONFIG = CONFIG
        self.runningSettings = runningSettings
        self.sourceName = ''

    def GenerateTests(self, count):
        pass


class CompilingTestGenerator(TestGenerator):
    def __init__(
            self,
            CONFIG,
            runningSettings
    ):
        TestGenerator.__init__(
            self,
            CONFIG,
            runningSettings,
        )

    def createRunner(self):
        return CompilerRunner(
            self.runningSettings
        )


class InterpretingTestGenerator(TestGenerator):
    def __init__(
            self,
            CONFIG,
            runningSettings,
    ):
        TestGenerator.__init__(
            self,
            CONFIG,
            runningSettings
        )

    def createRunner(self):
        return InterpreterRunner(
            self.runningSettings
        )


class SomeAverageTestGenerator(TestGenerator):
    def __init__(
            self,
            CONFIG,
            runningSettings
    ):
        TestGenerator.__init__(
            self,
            CONFIG,
            runningSettings
        )

    def createRunner(self):
        return SomeAverageRunner(
            self.runningSettings
        )
