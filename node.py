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
    def __init__(self, ipAddress, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ipAddress = ipAddress
        self.port = port
        self.listenQueue = 5

        #binding the address (ipAddress, port) for listening
        self.sock.bind((self.ipAddress, self.port))
        self.sock.listen(self.listenQueue)


    #self explanatory setters bellow
    def sendMessage(self, message, destination, port):

        #pickling the Message
        pickledMsg = pickle.dumps(message)

        #sending message via temp socket
        tempSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tempSock.connect((destination, port))
        tempSock.send(pickledMsg)
        tempSock.close()


    def recvMessage(self):
        self.sock.listen(self.listenQueue)
        clientsocket, address = self.sock.accept()
        msg = clientsocket.recv(1024)
        unpickledMsg = pickle.loads(msg)
        clientsocket.close()
        return unpickledMsg


    #python special methods
    def __repr__(self):
        return f"node({self.sock})"


    def __str__(self):
        return f"Node Object\nSocket: {self.sock}\n"
