# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_round.ui'
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

class Ui_dial_round(object):
    def setupUi(self, dial_round):
        dial_round.setObjectName(_fromUtf8("dial_round"))
        dial_round.resize(847, 700)
        self.gridLayout = QtGui.QGridLayout(dial_round)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.table_paired_players = QtGui.QTableWidget(dial_round)
        self.table_paired_players.setColumnCount(4)
        self.table_paired_players.setObjectName(_fromUtf8("table_paired_players"))
        self.table_paired_players.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.table_paired_players.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table_paired_players.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table_paired_players.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.table_paired_players.setHorizontalHeaderItem(3, item)
        self.gridLayout.addWidget(self.table_paired_players, 0, 0, 1, 1)

        self.retranslateUi(dial_round)
        QtCore.QMetaObject.connectSlotsByName(dial_round)

    def retranslateUi(self, dial_round):
        dial_round.setWindowTitle(_translate("dial_round", "Dialog", None))
        item = self.table_paired_players.horizontalHeaderItem(0)
        item.setText(_translate("dial_round", "No.", None))
        item = self.table_paired_players.horizontalHeaderItem(1)
        item.setText(_translate("dial_round", "White player", None))
        item = self.table_paired_players.horizontalHeaderItem(2)
        item.setText(_translate("dial_round", "Result", None))
        item = self.table_paired_players.horizontalHeaderItem(3)
        item.setText(_translate("dial_round", "Black player", None))

