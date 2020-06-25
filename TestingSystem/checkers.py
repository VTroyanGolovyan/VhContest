from runners import CompilerRunner, InterpreterRunner, SomeAverageRunner


class Checker:
    def __init__(
            self,
            CONFIG,
            runningSettings,
    ):
        self.CONFIG = CONFIG
        self.runningSettings = runningSettings
        self.sourceName = ''

    def Check(self, count):
        pass


class CompilingChecker(Checker):
    def __init__(
            self,
            CONFIG,
            runningSettings,
    ):
        Checker.__init__(
            self,
            CONFIG,
            runningSettings,
        )

    def createRunner(self):
        return CompilerRunner(
            self.runningSettings
        )


class InterpretingChecker(Checker):
    def __init__(
            self,
            CONFIG,
            runningSettings,
    ):
        Checker.__init__(
            self,
            CONFIG,
            runningSettings,
        )

    def createRunner(self):
        return InterpreterRunner(
            self.runningSettings
        )


class SomeAverageChecker(Checker):
    def __init__(
            self,
            CONFIG,
            runningSettings
    ):
        Checker.__init__(
            self,
            CONFIG,
            runningSettings
        )

    def createRunner(self):
        return SomeAverageRunner(
            self.runningSettings
        )
