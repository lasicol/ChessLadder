# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_new_tournament.ui'
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

class Ui_dial_new_tournament(object):
    def setupUi(self, dial_new_tournament):
        dial_new_tournament.setObjectName(_fromUtf8("dial_new_tournament"))
        dial_new_tournament.resize(403, 302)
        self.buttonBox = QtGui.QDialogButtonBox(dial_new_tournament)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.splitter_2 = QtGui.QSplitter(dial_new_tournament)
        self.splitter_2.setGeometry(QtCore.QRect(45, 50, 161, 22))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.label_2 = QtGui.QLabel(self.splitter_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.edit_rounds = QtGui.QLineEdit(self.splitter_2)
        self.edit_rounds.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edit_rounds.setFont(font)
        self.edit_rounds.setObjectName(_fromUtf8("edit_rounds"))
        self.splitter = QtGui.QSplitter(dial_new_tournament)
        self.splitter.setGeometry(QtCore.QRect(48, 20, 221, 22))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label = QtGui.QLabel(self.splitter)
        self.label.setObjectName(_fromUtf8("label"))
        self.edit_tournament_name = QtGui.QLineEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edit_tournament_name.setFont(font)
        self.edit_tournament_name.setObjectName(_fromUtf8("edit_tournament_name"))

        self.retranslateUi(dial_new_tournament)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), dial_new_tournament.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), dial_new_tournament.accept)
        QtCore.QMetaObject.connectSlotsByName(dial_new_tournament)

    def retranslateUi(self, dial_new_tournament):
        dial_new_tournament.setWindowTitle(_translate("dial_new_tournament", "New...", None))
        self.label_2.setText(_translate("dial_new_tournament", "Number of rounds: ", None))
        self.label.setText(_translate("dial_new_tournament", "Tournament name:", None))

