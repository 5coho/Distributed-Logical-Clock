"""
--Node Class File--

This class provide the main functionality for message passing.
Create the socket for listening, sends message and receives messages.
For future: buffering or dynamic recv() parameter

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
    #need ip address and port for initialization. hostname instead of port
    #is sufficient.
    def __init__(self, ipAddress, port):
        self.ipAddress = ipAddress
        self.port = port
        self.listenQueue = 5

        #setting up socket stuff
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.ipAddress, self.port))
        self.sock.listen(self.listenQueue)


    #the main send message function. takes a message object, destination address
    #and port. pickles message object, creates a temporary socket for sending
    #then sends pickled message
    def sendMessage(self, message, destination, port):

        #pickling the Message
        pickledMsg = pickle.dumps(message)

        #sending message via temp socket
        tempSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tempSock.connect((destination, port))
        tempSock.send(pickledMsg)
        tempSock.close()


    #when called, this function blocks at self.sock.accept() until a connection
    #is established. msg is received and unpickled then returns a message Object
    #for future: incorporate some form of buffer or have prelimary message that
    #sends message size then update the recv() parameter
    def recvMessage(self):
        clientsocket, address = self.sock.accept()
        msg = clientsocket.recv(1024)
        unpickledMsg = pickle.loads(msg)
        clientsocket.close()
        return unpickledMsg


    #python special methods
    #object representation
    def __repr__(self):
        return f"node({self.sock})"


    #to String
    def __str__(self):
        return f"Node Object\nSocket: {self.sock}\n"
