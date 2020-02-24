import socket
import pickle
import threading
import sys


#message class for demo
class message:

    def __init__(self):
        self.senderName = ""
        self.msg = ""
        self.clockCount = 0
        self.mSize = 0

    def setSenderName(self, name):
        self.senderName = name

    def setMsg(self, msg):
        self.msg = msg

    def setClockCount(self, count):
        self.clockCount = count

    def getSenderName(self):
        return self.senderName

    def getMsg(self):
        return self.msg

    def getClockCount(self):
        return self.clockCount

    def __repr__(self):
        return f"message({self.senderName}, {self.clockCount}, {self.msg}, {self.mSize})"

    def __str__(self):
        return f"Message Object\nSender: {self.senderName}\nClock: {self.clockCount}\nMessage: {self.msg}\nSize: {self.mSize}"


#HOSTNAME = socket.gethostname()
nodeName = input("Set Node Alias> ")
HOSTNAME = input("hostname>")
PORT = int(input("listening port>"))
sPORT = int(input("send to port>"))
count = int(input("Clock Start>"))
print()

ADDRESS = (HOSTNAME, PORT)


#the count


#setting the listening socket
s = socket.socket()
s.bind(ADDRESS)

#printing some info
print(f"Running Node '{nodeName}'...")
print("hostname:         ", HOSTNAME)
print("listing port:     ", PORT)
print("sending to port:  ", sPORT)
print("clock start #:    ", count)
print()


def thread_receive(sock):
    global count
    sock.listen(5)
    while True:
        clientsocket, address = sock.accept()
        msg = clientsocket.recv(1024)
        unpickledMsg = pickle.loads(msg)
        print(f"{unpickledMsg.getClockCount()} {unpickledMsg.getSenderName()}> {unpickledMsg.getMsg()}", flush=True)
        count = max(count, unpickledMsg.getClockCount()) + 1
        print(count)
        clientsocket.close()


#starting the listening threading
thread = threading.Thread(target=thread_receive, args=(s,))
thread.start()


#create message
while True:
    theMessage = input()
    if theMessage == "q":
        s.close()
        sys.exit()

    #count incrementing
    count = count + 1

    #creating message object
    m = message()
    m.setMsg(theMessage)
    m.setSenderName(nodeName)
    m.setClockCount(count)

    #print for debugging
    #print(m)

    #pickle Object
    pickledMsg = pickle.dumps(m)
    #print(pickledMsg)

    #send message
    tempSock = socket.socket()
    tempSock.connect((HOSTNAME, sPORT))
    tempSock.send(pickledMsg)
    tempSock.close()
