from UI.py_dialog_players_ui import Ui_dial_list
from UI.py_dialog_add_player_ui import Ui_dial_add_player
from UI.py_dialog_new_tournament_ui import Ui_dial_new_tournament
from UI.py_dialog_make_pair_ui import Ui_dial_make_pair
from UI.py_dialog_round_ui import Ui_dial_round
from UI.py_dialog_input_results_ui import Ui_dial_input_results
from PyQt4 import QtGui, QtCore, Qt


class ChildPlayerList(QtGui.QDialog, Ui_dial_list):
    def __init__(self):
        super(ChildPlayerList, self).__init__(None)
        self.setupUi(self)
        head = self.player_list.horizontalHeader()
        head.setStretchLastSection(True)

    def closeEvent(self, evnt):
        self.deleteLater()


class ChildAddPlayer(QtGui.QDialog, Ui_dial_add_player):
    def __init__(self, fun_btn_add, fun_btn_ok):
        super(ChildAddPlayer, self).__init__(None)
        self.setupUi(self)
        self.fun_btn_add = fun_btn_add
        self.fun_btn_ok = fun_btn_ok
        self.setup()

    def setup(self):
        # other windows will be disabled whit the option
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.btnAdd.clicked.connect(self.fun_btn_add)
        self.btnOK.clicked.connect(self.fun_btn_ok)

    def closeEvent(self, evnt):
        self.label_status.setText('')


class ChildNewTournament(QtGui.QDialog, Ui_dial_new_tournament):
    def __init__(self, fun_btn_ok, fun_btn_cancel):
        super(ChildNewTournament, self).__init__(None)
        self.setupUi(self)
        self.fun_btn_ok = fun_btn_ok
        self.fun_btn_cancel = fun_btn_cancel
        self.setup()

    def setup(self):
        # other windows will be disabled whit the option
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.buttonBox.accepted.connect(self.fun_btn_ok)
        self.buttonBox.rejected.connect(self.fun_btn_cancel)

    def accept(self):
        pass


class ChildMakePair(QtGui.QDialog, Ui_dial_make_pair):
    def __init__(self, fun_btn_ok, fun_btn_cancel):
        super(ChildMakePair, self).__init__(None)
        self.setupUi(self)
        self.fun_btn_ok = fun_btn_ok
        self.fun_btn_cancel = fun_btn_cancel
        self.setup()

    def setup(self):
        # other windows will be disabled whit the option
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.buttonBox.accepted.connect(self.fun_btn_ok)
        self.buttonBox.rejected.connect(self.fun_btn_cancel)
        self.btn_moveRight.clicked.connect(self.btn_move_right_clicked)
        self.btn_moveLeft.clicked.connect(self.btn_move_left_clicked)

    def accept(self):
        pass

    def btn_move_right_clicked(self):
        item = self.listWidget_all.takeItem(self.listWidget_all.currentRow())
        if item is not None:
            self.listWidget_selected.addItem(item.text())
            # remove from listWidget_all
            item = None

    def btn_move_left_clicked(self):
        item = self.listWidget_selected.takeItem(self.listWidget_selected.currentRow())
        if item is not None:
            self.listWidget_all.addItem(item.text())
            # remove from listWidget_selected
            item = None


class ChildRound(QtGui.QDialog, Ui_dial_round):
    def __init__(self):
        super(ChildRound, self).__init__(None)
        self.setupUi(self)
        self.setup()

    def setup(self):
        pass


class ChildInputResults(QtGui.QDialog, Ui_dial_input_results):
    def __init__(self, fun_btn_ok, fun_btn_cancel):
        super(ChildInputResults, self).__init__(None)
        self.setupUi(self)

        self.fun_btn_ok = fun_btn_ok
        self.fun_btn_cancel = fun_btn_cancel
        self.setup()

    def setup(self):
        self.buttonBox.accepted.connect(self.fun_btn_ok)
        self.buttonBox.rejected.connect(self.fun_btn_cancel)

        self.btBlackWin.clicked.connect(self.btn_black_win_clicked)
        self.btBlackWin.setShortcut("C")

        self.btWhiteWin.clicked.connect(self.btn_white_win_clicked)
        self.btWhiteWin.setShortcut("Z")

        self.btDraw.clicked.connect(self.btn_draw_clicked)
        self.btDraw.setShortcut("X")

        r = self.table_paired_players_input.currentRow()
        self.table_paired_players_input.selectRow(r)

    def btn_black_win_clicked(self):
        r = self.table_paired_players_input.currentRow()
        self.table_paired_players_input.selectRow(r)
        self.table_paired_players_input.setItem(r, 2, QtGui.QTableWidgetItem("0-1"))
        self.table_paired_players_input.selectRow(r+1)

    def btn_white_win_clicked(self):
        r = self.table_paired_players_input.currentRow()
        self.table_paired_players_input.selectRow(r)
        self.table_paired_players_input.setItem(r, 2, QtGui.QTableWidgetItem("1-0"))
        self.table_paired_players_input.selectRow(r+1)

    def btn_draw_clicked(self):
        r = self.table_paired_players_input.currentRow()
        self.table_paired_players_input.selectRow(r)
        self.table_paired_players_input.setItem(r, 2, QtGui.QTableWidgetItem("0.5-0.5"))
        self.table_paired_players_input.selectRow(r + 1)

    def accept(self):
        pass

