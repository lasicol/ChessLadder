# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_players.ui'
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

class Ui_dialog_add(object):
    def setupUi(self, dialog_add):
        dialog_add.setObjectName(_fromUtf8("dialog_add"))
        dialog_add.resize(638, 521)
        self.gridLayout = QtGui.QGridLayout(dialog_add)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_3 = QtGui.QPushButton(dialog_add)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 4, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(dialog_add)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(dialog_add)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.tableWidget = QtGui.QTableWidget(dialog_add)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 4)

        self.retranslateUi(dialog_add)
        QtCore.QMetaObject.connectSlotsByName(dialog_add)

    def retranslateUi(self, dialog_add):
        dialog_add.setWindowTitle(_translate("dialog_add", "Form", None))
        self.pushButton_3.setText(_translate("dialog_add", "PushButton", None))
        self.pushButton_2.setText(_translate("dialog_add", "PushButton", None))
        self.pushButton.setText(_translate("dialog_add", "PushButton", None))

