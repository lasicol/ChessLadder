# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_input_results.ui'
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

class Ui_dial_input_results(object):
    def setupUi(self, dial_input_results):
        dial_input_results.setObjectName(_fromUtf8("dial_input_results"))
        dial_input_results.resize(654, 550)
        self.table_paired_players_input = QtGui.QTableWidget(dial_input_results)
        self.table_paired_players_input.setGeometry(QtCore.QRect(70, 10, 481, 411))
        self.table_paired_players_input.setColumnCount(3)
        self.table_paired_players_input.setObjectName(_fromUtf8("table_paired_players_input"))
        self.table_paired_players_input.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.table_paired_players_input.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table_paired_players_input.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table_paired_players_input.setHorizontalHeaderItem(2, item)
        self.layoutWidget = QtGui.QWidget(dial_input_results)
        self.layoutWidget.setGeometry(QtCore.QRect(190, 434, 320, 51))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btWhiteWin = QtGui.QPushButton(self.layoutWidget)
        self.btWhiteWin.setObjectName(_fromUtf8("btWhiteWin"))
        self.horizontalLayout.addWidget(self.btWhiteWin)
        self.btDraw = QtGui.QPushButton(self.layoutWidget)
        self.btDraw.setObjectName(_fromUtf8("btDraw"))
        self.horizontalLayout.addWidget(self.btDraw)
        self.btBlackWin = QtGui.QPushButton(self.layoutWidget)
        self.btBlackWin.setObjectName(_fromUtf8("btBlackWin"))
        self.horizontalLayout.addWidget(self.btBlackWin)
        self.btErase = QtGui.QPushButton(self.layoutWidget)
        self.btErase.setObjectName(_fromUtf8("btErase"))
        self.horizontalLayout.addWidget(self.btErase)
        self.buttonBox = QtGui.QDialogButtonBox(dial_input_results)
        self.buttonBox.setGeometry(QtCore.QRect(470, 510, 156, 23))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(dial_input_results)
        QtCore.QMetaObject.connectSlotsByName(dial_input_results)

    def retranslateUi(self, dial_input_results):
        dial_input_results.setWindowTitle(_translate("dial_input_results", "Dialog", None))
        item = self.table_paired_players_input.horizontalHeaderItem(0)
        item.setText(_translate("dial_input_results", "White player", None))
        item = self.table_paired_players_input.horizontalHeaderItem(1)
        item.setText(_translate("dial_input_results", "Result", None))
        item = self.table_paired_players_input.horizontalHeaderItem(2)
        item.setText(_translate("dial_input_results", "Black player", None))
        self.btWhiteWin.setText(_translate("dial_input_results", "1-0", None))
        self.btDraw.setText(_translate("dial_input_results", "0.5-0.5", None))
        self.btBlackWin.setText(_translate("dial_input_results", "0-1", None))
        self.btErase.setText(_translate("dial_input_results", "-:-", None))

