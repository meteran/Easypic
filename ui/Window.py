#!/usr/bin/python
# coding: utf-8
from PyQt4 import QtGui

from PyQt4.QtGui import QMainWindow

from MainWindow import Ui_MainWindow
from modules.helpers import FlowLayout


class WindowUi(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super(WindowUi, self).setupUi(MainWindow)
        self.items = []
        self.flowLayout = FlowLayout(self.photos)



class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = WindowUi()
        self.ui.setupUi(self)
