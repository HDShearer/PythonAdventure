# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userInterfaceUpdated.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import __main__ as game
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1206, 707)
        MainWindow.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 410, 1031, 22))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit.setObjectName("lineEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 1031, 391))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1206, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_Game = QtWidgets.QAction(MainWindow)
        self.actionSave_Game.setObjectName("actionSave_Game")
        self.actionLoad_Game = QtWidgets.QAction(MainWindow)
        self.actionLoad_Game.setObjectName("actionLoad_Game")
        self.actionEnter_current_command = QtWidgets.QAction(MainWindow)
        self.actionEnter_current_command.setObjectName("actionEnter_current_command")
        self.menuFile.addAction(self.actionSave_Game)
        self.menuFile.addAction(self.actionLoad_Game)
        self.menuFile.addSeparator()
        self.menuEdit.addAction(self.actionEnter_current_command)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionEnter_current_command.triggered.connect(lambda: self.appendTB(self.lineEdit.text()))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Type Here"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionSave_Game.setText(_translate("MainWindow", "Save Game"))
        self.actionSave_Game.setToolTip(_translate("MainWindow", "Save Game"))
        self.actionSave_Game.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionLoad_Game.setText(_translate("MainWindow", "Load Game"))
        self.actionEnter_current_command.setText(_translate("MainWindow", "Enter current command"))
        self.actionEnter_current_command.setShortcut(_translate("MainWindow", "Return"))

    def appendTB(self, text):
        tb = self.textBrowser
        tb.append('(current player will be here): ' + text)
        self.lineEdit.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
