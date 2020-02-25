"""
--Node Gui File--

The gui file which holds the node_gui class

This class creates functionality for the node gui Allowing Message sending
between nodes.

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
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi


#the node_gui class
class node_gui(QWidget):


    #constructor
    def __init__(self, nodeName, ipAddress, port, timestampStart, xStart, yStart):

        #set up
        super(node_gui, self).__init__()
        loadUi("nodeGUI.ui", self)
        self.move(xStart, yStart)
        self.setWindowTitle(nodeName)

        #variables from constructor arguments
        self.nodeName = nodeName
        self.ipAddress = ipAddress
        self.port = port
        self.clockCount = timestampStart

        #creating socket
        sock = socket.socket()

        #setting up labels for info
        self.label_nodeName.setText(nodeName)
        self.label_hostname.setText(socket.gethostname())
        self.label_ipAddress.setText(ipAddress)
        self.label_port.setText(str(port))
        self.lcd_timestamp.display(timestampStart)

        self._load_connects()


    #load connection for the send msg button
    def _load_connects(self):

        #for send message button clicked
        self.bttn_sendMessage.clicked.connect(self.bttn_sendMessage_clicked)
        self.bttn_sendMessage.setAutoDefault(True)

        #for hitting enter on button and within lineEdit_send
        self.lineEdit_send.returnPressed.connect(self.bttn_sendMessage.click)
        self.lineEdit_to.returnPressed.connect(self.bttn_sendMessage.click)
        self.lineEdit_toPort.returnPressed.connect(self.bttn_sendMessage.click)


    #creates functionality to the send message buttion
    @pyqtSlot()
    def bttn_sendMessage_clicked(self):
        print("Stuff is happening!!!!!", flush=True)

        self._updateClockCount()
        self.textEdit_received.insertHtml(f"<b>{self.clockCount} {self.nodeName}></b> {self.lineEdit_send.text()}<br>")
        self.lineEdit_send.clear()

    #function to update clockCount and lcd
    def _updateClockCount(self):
        self.clockCount = self.clockCount + 1
        self.lcd_timestamp.display(self.clockCount)
        print(str(self.clockCount), flush=True)
