# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_add_player.ui'
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

class Ui_dial_add_player(object):
    def setupUi(self, dial_add_player):
        dial_add_player.setObjectName(_fromUtf8("dial_add_player"))
        dial_add_player.resize(238, 205)
        dial_add_player.setMinimumSize(QtCore.QSize(238, 205))
        dial_add_player.setMaximumSize(QtCore.QSize(238, 205))
        dial_add_player.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.groupBox = QtGui.QGroupBox(dial_add_player)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 217, 121))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.edit_elo = QtGui.QLineEdit(self.groupBox)
        self.edit_elo.setGeometry(QtCore.QRect(70, 80, 128, 20))
        self.edit_elo.setObjectName(_fromUtf8("edit_elo"))
        self.edit_first = QtGui.QLineEdit(self.groupBox)
        self.edit_first.setGeometry(QtCore.QRect(70, 28, 128, 20))
        self.edit_first.setObjectName(_fromUtf8("edit_first"))
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(19, 80, 46, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.edit_last = QtGui.QLineEdit(self.groupBox)
        self.edit_last.setGeometry(QtCore.QRect(70, 54, 128, 20))
        self.edit_last.setObjectName(_fromUtf8("edit_last"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(19, 54, 46, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(19, 28, 46, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.splitter = QtGui.QSplitter(dial_add_player)
        self.splitter.setGeometry(QtCore.QRect(50, 150, 150, 23))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.btnOK = QtGui.QPushButton(self.splitter)
        self.btnOK.setObjectName(_fromUtf8("btnOK"))
        self.btnCancel = QtGui.QPushButton(self.splitter)
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))

        self.retranslateUi(dial_add_player)
        QtCore.QMetaObject.connectSlotsByName(dial_add_player)

    def retranslateUi(self, dial_add_player):
        dial_add_player.setWindowTitle(_translate("dial_add_player", "Add player", None))
        self.groupBox.setTitle(_translate("dial_add_player", "Dane", None))
        self.label_10.setText(_translate("dial_add_player", "Ranking:", None))
        self.label.setText(_translate("dial_add_player", "Nazwisko:", None))
        self.label_9.setText(_translate("dial_add_player", "Imie:", None))
        self.btnOK.setText(_translate("dial_add_player", "OK", None))
        self.btnCancel.setText(_translate("dial_add_player", "Anuluj", None))

