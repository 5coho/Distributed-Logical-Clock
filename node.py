"""
--Node Class File--

This class provide the main functionality for message passing.
the node_gui passes a socket object for Initialization and a message Object
for sending.

"""


#Metadata
__author__          = "Scott Howes"
__credits__         = "Scott Howes"
__email__           = "showes@unbc.ca"
__python_version__  = "3.8.1"


#imports
import pickle
import socket


#message class for demo
class node:


    #constructor
    def __init__(self, socket):
        self.sock = socket


    #self explanatory setters bellow
    def sendMessage(self, message):
        pass


    def recvMessage(self):
        pass


    #python special methods
    def __repr__(self):
        return f"node({self.sock})"


    def __str__(self):
        return f"Node Object\nSocket: {self.sock}\nClock: {self.clockCount}\nMessage: {self.msg}\nSize: {self.mSize}"
