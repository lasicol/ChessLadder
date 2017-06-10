# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_make_pair.ui'
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

class Ui_dial_make_pair(object):
    def setupUi(self, dial_make_pair):
        dial_make_pair.setObjectName(_fromUtf8("dial_make_pair"))
        dial_make_pair.resize(494, 595)
        self.buttonBox = QtGui.QDialogButtonBox(dial_make_pair)
        self.buttonBox.setGeometry(QtCore.QRect(40, 550, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.spinBox = QtGui.QSpinBox(dial_make_pair)
        self.spinBox.setGeometry(QtCore.QRect(170, 40, 42, 22))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.label = QtGui.QLabel(dial_make_pair)
        self.label.setGeometry(QtCore.QRect(129, 44, 41, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.listWidget_all = QtGui.QListWidget(dial_make_pair)
        self.listWidget_all.setGeometry(QtCore.QRect(10, 100, 191, 411))
        self.listWidget_all.setObjectName(_fromUtf8("listWidget_all"))
        self.btn_moveRight = QtGui.QPushButton(dial_make_pair)
        self.btn_moveRight.setGeometry(QtCore.QRect(210, 240, 31, 31))
        self.btn_moveRight.setObjectName(_fromUtf8("btn_moveRight"))
        self.btn_moveLeft = QtGui.QPushButton(dial_make_pair)
        self.btn_moveLeft.setGeometry(QtCore.QRect(210, 280, 31, 31))
        self.btn_moveLeft.setObjectName(_fromUtf8("btn_moveLeft"))
        self.listWidget_selected = QtGui.QListWidget(dial_make_pair)
        self.listWidget_selected.setGeometry(QtCore.QRect(250, 100, 191, 411))
        self.listWidget_selected.setObjectName(_fromUtf8("listWidget_selected"))

        self.retranslateUi(dial_make_pair)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), dial_make_pair.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), dial_make_pair.reject)
        QtCore.QMetaObject.connectSlotsByName(dial_make_pair)

    def retranslateUi(self, dial_make_pair):
        dial_make_pair.setWindowTitle(_translate("dial_make_pair", "Dialog", None))
        self.label.setText(_translate("dial_make_pair", "Round:", None))
        self.btn_moveRight.setText(_translate("dial_make_pair", ">>", None))
        self.btn_moveLeft.setText(_translate("dial_make_pair", "<<", None))

