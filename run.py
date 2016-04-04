#!/usr/bin/python
# coding: utf-8
from PyQt4 import QtGui

from ui.Window import Window



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())