#!/usr/bin/python
# coding: utf-8
import sys
from PyQt4 import QtGui

from ui.App import App

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
