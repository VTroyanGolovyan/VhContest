import subprocess


class RunningSettings:
    def __init__(
            self,
            runningType,
            compilerBash,
            interpreterBash,
            checkSyntaxBash,
    ):
        self.runningType = runningType          # Running type
        self.compilerBash = compilerBash        # Compilation bash command
        self.interpreterBash = interpreterBash  # Interpreter bash command
        self.checkSyntaxBash = checkSyntaxBash  # Check syntax bash


class BaseRunner:
    def __init__(
            self,
            runningSettings,
            controllerBinPath,
            runningPath,
            sourceFile,
            timeLimit,
            memoryLimit,
            processLimit
    ):
        self.settings = runningSettings
        self.controllerBash = controllerBinPath
        self.runningPath = runningPath
        self.sourceFile = sourceFile
        self.timeLimit = timeLimit
        self.memoryLimit = memoryLimit
        self.processLimit = processLimit

    def checkSyntax(self):
        raise Exception('Check syntax method doesn\'t implemented')

    def runProgram(self):
        raise Exception('Run program doesn\'t implemented')

    def setInput(self, inputString):
        try:
            f = open(self.settings.runningPath + 'input.txt', 'w')
            f.write(inputString)
            f.close()
        except Exception:
            raise Exception('Error with creating file')

    def getOutput(self):
        try:
            f = open(self.settings.runningPath + 'output.txt', 'r')
            return f.readlines()
        except Exception:
            raise Exception('Error with reading file')


class CompilerRunner(BaseRunner):
    def __init__(
            self,
            runningSettings,
            controllerBinPath,
            runningPath,
            sourceFile,
            timeLimit,
            memoryLimit,
            processLimit
    ):
        BaseRunner.__init__(
            self,
            runningSettings,
            controllerBinPath,
            runningPath,
            sourceFile,
            timeLimit,
            memoryLimit,
            processLimit
        )

    def checkSyntax(self):
        bashCommand = self.settings.checkSyntaxBash + ' ' + self.runningPath + '/' + self.sourceFile
        process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

    def runProgram(self):
        pass


class InterpreterRunner(BaseRunner):
    def __init__(
            self,
            runningSettings,
            controllerBinPath,
            runningPath,
            sourceFile,
            timeLimit,
            memoryLimit,
            processLimit
    ):
        BaseRunner.__init__(
            self,
            runningSettings,
            controllerBinPath,
            runningPath,
            sourceFile,
            timeLimit,
            memoryLimit,
            processLimit
        )

    def checkSyntax(self):
        bashCommand = self.settings.checkSyntaxBash + ' ' + self.runningPath + '/' + self.sourceFile
        process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

    def runProgram(self):
        pass


class SomeAverageRunner(BaseRunner):
    def __init__(
            self,
            runningSettings,
            controllerBinPath,
            runningPath,
            sourceFile,
            timeLimit,
            memoryLimit,
            processLimit
    ):
        BaseRunner.__init__(
            self,
            runningSettings,
            controllerBinPath,
            runningPath,
            sourceFile,
            timeLimit,
            memoryLimit,
            processLimit
        )

    def checkSyntax(self):
        bashCommand = self.settings.checkSyntaxBash + ' ' + self.runningPath + '/' + self.sourceFile
        process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

    def runProgram(self):
        pass
