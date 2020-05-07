import subprocess
import resource
from process_monitor import ProcessMonitor


def preexecCallback(cpu, memory, childs):
    # rlimit cpu works in seconds
    if cpu - int(cpu) > 0:
        cpu += 1

    def limiter():
        resource.setrlimit(resource.RLIMIT_CPU, (cpu, cpu))
    return limiter


class RunningSettings:
    def __init__(
            self,
            runningType,
            compilerBash,
            interpreterBash,
            checkSyntaxBash,
            fileEnd
    ):
        self.runningType = runningType          # Running type
        self.compilerBash = compilerBash        # Compilation bash command
        self.interpreterBash = interpreterBash  # Interpreter bash command
        self.checkSyntaxBash = checkSyntaxBash  # Check syntax bash
        self.fileEnd = fileEnd                  # f. e. cpp


class BaseRunner:
    def __init__(
            self,
            runningSettings
    ):
        self.settings = runningSettings

    def checkSyntax(self):
        raise Exception('Check syntax method doesn\'t implemented')

    def runProgram(self, directory, path, testStdin, timeout, memory):
        bashCommand = self.getBash(directory, path)
        process = subprocess.Popen(
            bashCommand,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            executable='/bin/bash',
            preexec_fn=preexecCallback(timeout + 0.1, 1, 0)
        )
        monitor = ProcessMonitor(process)
        monitor.start()
        process.stdin.write(testStdin.encode('utf-8'))
        try:
            output, error = process.communicate(timeout=(timeout + 0.1))
            print(monitor.cpu, timeout)
            if memory < monitor.rss // 1024 // 1024:
                return output, error, 'ML', monitor.rss, monitor.cpu
            if error.decode('utf-8') != '':
                if monitor.cpu >= timeout:
                    return output, error, 'TL', monitor.rss, timeout
                return output, error, 'RE', monitor.rss, monitor.cpu
            return output, error, 'NL', monitor.rss, monitor.cpu
        except subprocess.TimeoutExpired:
            process.kill()
            output, error = process.communicate()
            print(error)
            return output, error, 'TL', monitor.rss, monitor.cpu
        except Exception:
            return '', '', 'RE', monitor.rss, monitor.cpu

    def getBash(self, testingPath, source):
        return self.settings.interpreterBash.format(testingPath, source)


class InterpreterRunner(BaseRunner):
    def __init__(
            self,
            runningSettings
    ):
        BaseRunner.__init__(
            self,
            runningSettings
        )

    def checkSyntax(self):
        pass

    def getBash(self, testingPath, source):
        return self.settings.interpreterBash.format(testingPath, source)


class CompilerRunner(BaseRunner):
    def __init__(
            self,
            runningSettings
    ):
        BaseRunner.__init__(
            self,
            runningSettings
        )

    def getBash(self, testingPath, source):
        return self.settings.interpreterBash.format(testingPath, source)


class SomeAverageRunner(BaseRunner):
    def __init__(
            self,
            runningSettings
    ):
        BaseRunner.__init__(
            self,
            runningSettings
        )

    def getBash(self, testingPath, source):
        return self.settings.interpreterBash.format(testingPath, source)
