#Kill a process with process name
import psutil
def kill():
    for process in psutil.process_iter():
        if process.name() == "Calculator.exe":
            process.kill()
            return True
        else:
            return False
print(kill())

#notepad.exe,Calculator.exe,
