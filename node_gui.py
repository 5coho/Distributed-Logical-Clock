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
import os
import socket
import threading
from message import message
from node import node
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi


#the node_gui class
class node_gui(QWidget):


    #constructor
    def __init__(self, nodeName, ipAddress, port, timestampStart, xStart, yStart):
        super(node_gui, self).__init__()
        loadUi("GUIs/nodeGUI.ui", self)
        self.move(xStart, yStart)
        self.setWindowIcon(QIcon("media/icon.png"))
        self.setWindowTitle(f"{nodeName} - PID:{os.getpid()}")

        #variables from constructor arguments
        self.nodeName = nodeName
        self.ipAddress = ipAddress
        self.port = port
        self.clockCount = timestampStart

        #checks if ipAddress is Loopback. changes lineEdit_to accordingly
        if ipAddress == "127.0.0.1":
            self.lineEdit_to.setText("127.0.0.1")

        #creating node Object
        self.node = node(self.ipAddress, self.port)

        #creating message object
        self.message = message()
        self.message.setSenderName(self.nodeName)

        #setting up labels for info
        self.label_nodeName.setText(self.nodeName)
        self.label_hostname.setText(socket.gethostname())
        self.label_ipAddress.setText(self.ipAddress)
        self.label_port.setText(str(self.port))
        self.lcd_timestamp.display(self.clockCount)

        #load connections
        self._load_connects()

        #starting listening thread
        self.thread = threading.Thread(target=self._thread_receive, args=(), daemon=True)
        self.thread.start()


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

        #event is known, update timestamp
        self.clockCount = self.clockCount + 1
        self.lcd_timestamp.display(self.clockCount)

        #logic for message sending goes here
        self.message.setMsg(self.lineEdit_send.text())
        self.message.setClockCount(self.clockCount)
        self.node.sendMessage(self.message, self.lineEdit_to.text(), int(self.lineEdit_toPort.text()))

        #printing sent message to textEdit_received
        self.textEdit_received.insertHtml(f"<b>{self.clockCount} {self.nodeName}></b> {self.lineEdit_send.text()}<br>")
        self.lineEdit_send.clear()


    #the function that will execute in a concurrent thread that
    #will listen for connections and updates the gui accordingly
    def _thread_receive(self):
        while True:
            message = self.node.recvMessage()
            self.clockCount = max(message.getClockCount(), self.clockCount) + 1
            self.lcd_timestamp.display(self.clockCount)
            self.textEdit_received.insertHtml(f"<b>{self.clockCount} {message.getSenderName()}></b> {message.getMsg()}<br>")
