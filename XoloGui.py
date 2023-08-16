
from XoloUi import Ui_XoloUi
from PyQt5 import QtCore , QtGui , QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt , QTimer , QTime , QDate
from PyQt5.uic import loadUiType
import os
import sys
import main 

class MainThread(QThread):

    def __init__(self):
        super(MainThread,self).__init__()     
    def run(self):   
        os.startfile(r"C:\Users\r1ash\OneDrive\Desktop\JUI\main.py")

startExe = MainThread()

class Gui_Start(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.gui = Ui_XoloUi()
        self.gui.setupUi(self)
        self.gui.pushButton_1.clicked.connect(self.startTask)
        self.gui.pushButton_2 .clicked.connect(self.close)       

    def startTask(self):
         startExe.start()

GuiApp = QApplication(sys.argv)
Xolo_gui = Gui_Start()
Xolo_gui.show()
exit(GuiApp.exec_())
