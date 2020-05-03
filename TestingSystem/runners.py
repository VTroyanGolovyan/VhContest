import subprocess
import resource
from process_monitor import ProcessMonitor


def preexecCallback(time, memory, childs):
    def limiter():
        resource.setrlimit(resource.RLIMIT_CPU, (time, time))
        resource.setrlimit(resource.RLIMIT_NPROC, (childs, childs))
    return limiter


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
            timeLimit,
            memoryLimit,
            processLimit
    ):
        self.settings = runningSettings
        self.controllerBash = controllerBinPath
        self.timeLimit = timeLimit
        self.memoryLimit = memoryLimit
        self.processLimit = processLimit

    def checkSyntax(self):
        raise Exception('Check syntax method doesn\'t implemented')

    def runProgram(self, path, stdin, timeout, memory):
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
            timeLimit,
            memoryLimit,
            processLimit
    ):
        BaseRunner.__init__(
            self,
            runningSettings,
            controllerBinPath,
            timeLimit,
            memoryLimit,
            processLimit
        )

    def checkSyntax(self):
        pass

    def runProgram(self, path, stdin, timeout, memory):
        pass


class InterpreterRunner(BaseRunner):
    def __init__(
            self,
            runningSettings,
            controllerBinPath,
            timeLimit,
            memoryLimit,
            processLimit
    ):
        BaseRunner.__init__(
            self,
            runningSettings,
            controllerBinPath,
            timeLimit,
            memoryLimit,
            processLimit
        )

    def checkSyntax(self):
        pass

    def runProgram(self, path, test_stdin, timeout, memory):
        bashCommand = self.settings.interpreterBash.format(path)
        process = subprocess.Popen(
            bashCommand,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            executable='/bin/bash',
            preexec_fn=preexecCallback(timeout * 2, 1, 0)
        )
        monitor = ProcessMonitor(process)
        monitor.start()
        process.stdin.write(test_stdin.encode('utf-8'))
        try:
            output, error = process.communicate(timeout= timeout + 0.1)
            if memory < monitor.rss // 1024 // 1024:
                return output, error, 'ML', monitor.rss, monitor.cpu
            if error.decode('utf-8') != '':
                return output, error, 'RE', monitor.rss, monitor.cpu
            return output, error, 'NL', monitor.rss, monitor.cpu
        except subprocess.TimeoutExpired:
            process.kill()
            output, error = process.communicate()
            return output, error, 'TL', monitor.rss, monitor.cpu
        except Exception:
            return '', '', 'RE', monitor.rss, monitor.cpu


class SomeAverageRunner(BaseRunner):
    def __init__(
            self,
            runningSettings,
            controllerBinPath,
            timeLimit,
            memoryLimit,
            processLimit
    ):
        BaseRunner.__init__(
            self,
            runningSettings,
            controllerBinPath,
            timeLimit,
            memoryLimit,
            processLimit
        )

    def checkSyntax(self):
        pass

    def runProgram(self, path, stdin, timeout, memory):
        pass
