# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1089, 729)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.photos = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.photos.sizePolicy().hasHeightForWidth())
        self.photos.setSizePolicy(sizePolicy)
        self.photos.setMinimumSize(QtCore.QSize(0, 0))
        self.photos.setTabShape(QtGui.QTabWidget.Rounded)
        self.photos.setDocumentMode(False)
        self.photos.setTabsClosable(True)
        self.photos.setMovable(True)
        self.photos.setObjectName(_fromUtf8("photos"))
        self.view_1 = QtGui.QWidget()
        self.view_1.setObjectName(_fromUtf8("view_1"))
        self.photos.addTab(self.view_1, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.photos, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1089, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuPlik = QtGui.QMenu(self.menubar)
        self.menuPlik.setObjectName(_fromUtf8("menuPlik"))
        self.menuEdycja = QtGui.QMenu(self.menubar)
        self.menuEdycja.setObjectName(_fromUtf8("menuEdycja"))
        self.menuWidok = QtGui.QMenu(self.menubar)
        self.menuWidok.setObjectName(_fromUtf8("menuWidok"))
        self.menuUstawienia = QtGui.QMenu(self.menubar)
        self.menuUstawienia.setObjectName(_fromUtf8("menuUstawienia"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_4 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_4.setMinimumSize(QtCore.QSize(298, 154))
        self.dockWidget_4.setAutoFillBackground(False)
        self.dockWidget_4.setStyleSheet(_fromUtf8(""))
        self.dockWidget_4.setFloating(False)
        self.dockWidget_4.setObjectName(_fromUtf8("dockWidget_4"))
        self.dockWidgetContents_5 = QtGui.QWidget()
        self.dockWidgetContents_5.setObjectName(_fromUtf8("dockWidgetContents_5"))
        self.gridLayout_5 = QtGui.QGridLayout(self.dockWidgetContents_5)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.tabWidget = QtGui.QTabWidget(self.dockWidgetContents_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMaximumSize(QtCore.QSize(500, 16777215))
        self.tabWidget.setBaseSize(QtCore.QSize(0, 0))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.directories = QtGui.QTreeWidget(self.tab)
        self.directories.setGeometry(QtCore.QRect(9, 9, 256, 192))
        self.directories.setFrameShape(QtGui.QFrame.NoFrame)
        self.directories.setFrameShadow(QtGui.QFrame.Plain)
        self.directories.setObjectName(_fromUtf8("directories"))
        self.directories.headerItem().setText(0, _fromUtf8("1"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout = QtGui.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Albums = QtGui.QListWidget(self.tab_2)
        self.Albums.setFrameShape(QtGui.QFrame.NoFrame)
        self.Albums.setFrameShadow(QtGui.QFrame.Plain)
        self.Albums.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.Albums.setObjectName(_fromUtf8("Albums"))
        self.gridLayout.addWidget(self.Albums, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout_5.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.dockWidget_4.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_4)
        self.dockWidget_2 = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_2.sizePolicy().hasHeightForWidth())
        self.dockWidget_2.setSizePolicy(sizePolicy)
        self.dockWidget_2.setMinimumSize(QtCore.QSize(87, 109))
        self.dockWidget_2.setAccessibleName(_fromUtf8(""))
        self.dockWidget_2.setFloating(False)
        self.dockWidget_2.setObjectName(_fromUtf8("dockWidget_2"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.info = QtGui.QTextBrowser(self.dockWidgetContents_2)
        self.info.setMaximumSize(QtCore.QSize(3423423, 16777215))
        self.info.setAutoFillBackground(False)
        self.info.setFrameShape(QtGui.QFrame.NoFrame)
        self.info.setFrameShadow(QtGui.QFrame.Plain)
        self.info.setLineWidth(1)
        self.info.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.info.setObjectName(_fromUtf8("info"))
        self.gridLayout_4.addWidget(self.info, 0, 0, 1, 1)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_2)
        self.menubar.addAction(self.menuPlik.menuAction())
        self.menubar.addAction(self.menuEdycja.menuAction())
        self.menubar.addAction(self.menuWidok.menuAction())
        self.menubar.addAction(self.menuUstawienia.menuAction())

        self.retranslateUi(MainWindow)
        self.photos.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Easypic", None))
        self.photos.setTabText(self.photos.indexOf(self.view_1), _translate("MainWindow", "widok", None))
        self.menuPlik.setTitle(_translate("MainWindow", "Plik", None))
        self.menuEdycja.setTitle(_translate("MainWindow", "Edycja", None))
        self.menuWidok.setTitle(_translate("MainWindow", "Widok", None))
        self.menuUstawienia.setTitle(_translate("MainWindow", "Ustawienia", None))
        self.dockWidget_4.setWindowTitle(_translate("MainWindow", "nawigacja", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Katalogi", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Albumy", None))
        self.dockWidget_2.setWindowTitle(_translate("MainWindow", "info", None))


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
