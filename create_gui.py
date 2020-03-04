"""
--Create Node Gui File--

The gui file which holds the create_gui class

The create_gui class creates the functionality for the createGUI.ui file.
This class creates nodes in the [simulated] distributed system allowing
one to set IP, node name, port, and timestamp start.

sockets created are IPv4 Family and use TCP protocol.

"""


#Metadata
__author__          = "Scott Howes"
__credits__         = "Scott Howes"
__email__           = "showes@unbc.ca"
__python_version__  = "3.8.1"


#imports
import sys
import time
import socket
from node_gui import node_gui
from multiprocessing import Process
import threading
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QProcess
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi


#the create_gui class
class create_gui(QWidget):


    #constructor
    def __init__(self):
        super(create_gui, self).__init__()
        loadUi("createGUI.ui", self)
        self.radioBttn_hostName.setText(f"{socket.gethostname()} ({socket.gethostbyname(socket.gethostname())})")
        self._load_connects()
        self.move(20,20)
        self.nodeThread = Thread()


    #loads the connection for the buttion
    def _load_connects(self):

        #bttn_create connects
        self.bttn_create.clicked.connect(self.bttn_create_clicked)
        self.bttn_create.setAutoDefault(True)

        #pressing enter in lineEdits runs bttn_create_clicked()
        self.lineEdit_name.returnPressed.connect(self.bttn_create.click)
        self.lineEdit_port.returnPressed.connect(self.bttn_create.click)
        self.lineEdit_timeStart.returnPressed.connect(self.bttn_create.click)


    #function for the node process to be created
    def create_node(self):
        print("Creating new node...", flush=True)
        proc = QProcess()
        proc.start(self.testProc())
        proc.kill()
        #NodeApp = QApplication(sys.argv)
        #gui = node_gui("Ricky Martin", "127.0.0.1", 1234, 0, 20, 360)
        #gui.show()
        #sys.exit(NodeApp.exec_())


    def testProc(self):
        print("starting process...", flush=True)
        print("sleeping for 3 seconds...", flush=True)
        time.sleep(3)
        print("Killing process", flush=True)
        #NodeApp = QApplication(sys.argv)
        #gui1 = node_gui("Ricky Martin", "127.0.0.1", 1234, 0, 20, 360)
        #gui1.show()
        #sys.exit(NodeApp.exec_())
        #nodeThread = Thread()
        #nodeThread.start()


    #this function updates the lineEdit fields
    #just increments lineEdit_port by one to ensure distinct nodes ports
    def _updateNamePort(self):
        portNum = int(self.lineEdit_port.text())
        portNum = portNum + 1
        self.lineEdit_port.setText(str(portNum))


    #creates the functionality for the create Node button
    @pyqtSlot()
    def bttn_create_clicked(self):

        #checking which radio button is checked
        if self.radioBttn_hostName.isChecked():
            ipAddress = socket.gethostname()
        else:
            ipAddress = "127.0.0.1"

        #checking port is not in privileged
        if int(self.lineEdit_port.text()) <= 1023:
            self.textEdit_log.insertHtml(f"Node <b>{self.lineEdit_name.text()}@{ipAddress}:{self.lineEdit_port.text()}</b> could not be created. Port must be greater than 1023!<br />")
            self.lineEdit_port.setText("1024")
            return

        #open node window (multiprocessing)
        #nodeProcess = Process(target=self.testProc, args=())
        #nodeProcess.start()
        #nodeProcess.join()

        #thread = threading.Thread(target=self.testProc, args=())
        #thread.start()
        #thread.join()

        #proc = QProcess()
        #proc.start(self.testProc())
        #proc.kill()

        #nodeThread = Thread()
        #self.nodeThread.start()

        #nodeApp = QApplication(sys.argv)
        #gui1 = node_gui("Ricky Martin", "127.0.0.1", 1234, 0, 20, 360)
        #gui1.show()
        #sys.exit(nodeApp.exec_())

        #printing to textEdit_log
        self.textEdit_log.insertHtml(f"Node <b>{self.lineEdit_name.text()}@{ipAddress}:{self.lineEdit_port.text()}</b> created. Timestamp starting at <b>{self.lineEdit_timeStart.text()}</b><br />")
        self._updateNamePort()



#Test thread
#fuckkkkkkkkkkkkk
class Thread(QThread):

    def __init__(self):
        super(Thread, self).__init__()

    def run(self):
        #print("starting process...", flush=True)
        #print("sleeping for 3 seconds...", flush=True)
        #time.sleep(3)
        #print("Killing process", flush=True)
        #sprint("printing stuff...", flush=True)
        nodeApp = QApplication(sys.argv)
        gui1 = node_gui("Ricky Martin", "127.0.0.1", 1234, 0, 20, 360)
        gui1.show()
        sys.exit(nodeApp.exec_())
        #return
