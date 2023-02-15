
# (test) C:\Users\jack-kt.wong\gui_example>python C:\Users\jack-kt.wong\AppData\Local\conda\conda\envs\test\Library\bin\pyside2-uic mainWindow.ui 
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Mon Oct 22 21:31:40 2018
#      by: pyside2-uic 2.0.0 running on PySide2 5.6.0~a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(753, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.goButton = QtWidgets.QPushButton(self.centralwidget)
        self.goButton.setGeometry(QtCore.QRect(300, 310, 75, 23))
        self.goButton.setObjectName("goButton")
        self.goText = QtWidgets.QTextEdit(self.centralwidget)
        self.goText.setGeometry(QtCore.QRect(80, 50, 511, 241))
        self.goText.setObjectName("goText")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 753, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.goButton.setText(QtWidgets.QApplication.translate("MainWindow", "Go Button", None, -1))

