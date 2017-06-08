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

class Ui_dial_list(object):
    def setupUi(self, dial_list):
        dial_list.setObjectName(_fromUtf8("dial_list"))
        dial_list.resize(638, 521)
        self.gridLayout = QtGui.QGridLayout(dial_list)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.player_list = QtGui.QTableWidget(dial_list)
        self.player_list.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.player_list.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.player_list.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
        self.player_list.setObjectName(_fromUtf8("player_list"))
        self.player_list.setColumnCount(0)
        self.player_list.setRowCount(0)
        self.gridLayout.addWidget(self.player_list, 0, 0, 1, 2)

        self.retranslateUi(dial_list)
        QtCore.QMetaObject.connectSlotsByName(dial_list)

    def retranslateUi(self, dial_list):
        dial_list.setWindowTitle(_translate("dial_list", "List of players", None))

