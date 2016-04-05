#!/usr/bin/python
# coding: utf-8
from PyQt4.QtGui import QMainWindow

from MainWindow import Ui_MainWindow
from modules.compute import Compute
from modules.filter import Filter
from modules.helpers import FlowLayout
from modules.session import Session


class WindowUi(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super(WindowUi, self).setupUi(MainWindow)
        self.items = []
        self.flowLayout = FlowLayout(self.photos)


class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = WindowUi()
        self.ui.setupUi(self)

        self.session = Session()
        self.compute = Compute()
        self.filter = Filter()
