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
def main():
    app = QApplication(sys.argv)
    gui = create_gui()
    gui.show()
    sys.exit(app.exec_())


#running main()
if __name__ == "__main__":
    main()
