"""
--The main file--

To start the program run this file

Creates The QApplication, Initializes GUI, the displays it.
Only opens the createGUI.

"""


#Metadata
__author__          = "Scott Howes"
__credits__         = "Scott Howes"
__email__           = "showes@unbc.ca"
__python_version__  = "3.8.1"


#imports go here
import sys
import multiprocessing
from create_gui import create_gui
from node_gui import node_gui
from PyQt5.QtWidgets import QApplication


#defining the main function
#creates and shows the create node gui

def process1():
    app = QApplication(sys.argv)
    gui = node_gui("Ricky Martin", "127.0.0.1", 1234, 0, 20, 280)
    gui.show()
    sys.exit(app.exec_())

def process2():
    app = QApplication(sys.argv)
    gui = node_gui("Graeme Morgan", "127.0.0.1", 1235, 0, 583, 280)
    gui.show()
    sys.exit(app.exec_())

def process3():
    app = QApplication(sys.argv)
    gui = node_gui("Shakira", "127.0.0.1", 1236, 12, 1146, 280)
    gui.show()
    sys.exit(app.exec_())

def main2():
    proc1 = multiprocessing.Process(target=process1)
    proc2 = multiprocessing.Process(target=process2)
    proc3 = multiprocessing.Process(target=process3)
    proc1.start()
    proc2.start()
    proc3.start()
    sys.exit()

def main1():
    app = QApplication(sys.argv)
    gui = create_gui()
    gui.show()
    sys.exit(app.exec_())


#running main()
if __name__ == "__main__":
    main2()
