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
    def __init__(self):
        super(node_gui, self).__init__()
        loadUi("nodeGUI.ui", self)


    #load connections functions
    def _load_connects(self):
        pass
