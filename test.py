from PyQt5.QtCore import QProcess
import os

def process1():
    print(f"starting process 1: {os.getpid()} {proc1.processId()}")

def process2():
    print(f"starting process 2: {os.getpid()} {proc1.processId()}")

proc1 = QProcess()
#proc2 = QProcess()
proc1.startDetached(process1())
proc1.startDetached(process2())
print(proc1.processId())
#print(proc2.processId())
