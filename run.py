
import mainClasses
from UI.py_main_ui import Ui_MainWindow
from UI.py_dialog_players_ui import Ui_dial_list
from UI.py_dialog_add_player_ui import Ui_dial_add_player
from UI.py_dialog_new_tournament_ui import Ui_dial_new_tournament
from PyQt4 import QtGui, Qt, QtCore
import sys


class ChildPlayerList(QtGui.QDialog, Ui_dial_list):
    def __init__(self):
        super(ChildPlayerList, self).__init__(None)
        self.setupUi(self)


class ChildAddPlayer(QtGui.QDialog, Ui_dial_add_player):
    def __init__(self, fun_btn_ok, fun_btn_cancel):
        super(ChildAddPlayer, self).__init__(None)
        self.setupUi(self)
        self.fun_btn_ok = fun_btn_ok
        self.fun_btn_cancel = fun_btn_cancel
        self.setup()

    def setup(self):
        # other windows will be disabled whit the option
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.btnOK.clicked.connect(self.fun_btn_ok)
        self.btnCancel.clicked.connect(self.fun_btn_cancel)


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



class MyApp(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Dialogs
        self.dial_player_list = None
        self.dial_add_player = None
        self.dial_new_tournament = None

        # Tournament
        self.isTournament = True
        self.T = None

        # Toolbar actions:
        self.act_add_player = QtGui.QIcon()
        self.act_list = QtGui.QIcon()

        self.setup()
        self.update()

    def setup(self):
        self.set_toolbar()

    def update(self):
        if not self.isTournament:
            self.toolBar.setEnabled(False)

    def run(self):
        self.actionNew_tournament.triggered.connect(self.act_new_tournament_clicked)
        # self.dial_add_player.closeEvent.connect(self.closing_dial_add_player)


    def set_toolbar(self):
        # Add player
        self.act_add_player = QtGui.QAction(QtGui.QIcon("Graph\icAddUser.png"), "new user", self)
        self.toolBar.addAction(self.act_add_player)
        self.act_add_player.triggered.connect(self.act_add_player_clicked)

        # List
        self.act_list = QtGui.QAction(QtGui.QIcon("Graph\icList.png"), "show list", self)
        self.toolBar.addAction(self.act_list)
        self.act_list.triggered.connect(self.act_list_clicked)

    def add_to_list(self, list_of_string):
        for i in list_of_string:
            self.listWidget.addItem(i.str_with_rank())

    def set_table_widget(self, list_, table_widget):
        table_widget.setRowCount(100)
        table_widget.setColumnCount(5)
        table_widget.setHorizontalHeaderLabels(['ID', 'RANK', 'FIRST NAME', 'LAST NAME', 'ELO'])
        table_widget.verticalHeader().setVisible(False)
        table_widget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        for i, ppl in enumerate(list_):
            table_widget.setItem(i, 0, QtGui.QTableWidgetItem(str(ppl.id)))
            table_widget.setItem(i, 1, QtGui.QTableWidgetItem(str(ppl.rank)))
            table_widget.setItem(i, 2, QtGui.QTableWidgetItem(str(ppl.first_name)))
            table_widget.setItem(i, 3, QtGui.QTableWidgetItem(str(ppl.last_name)))
            table_widget.setItem(i, 4, QtGui.QTableWidgetItem(str(ppl.elo)))
        # item = QtGui.QTableWidgetItem("lody")
        # self.tableWidget.setItem(1,0,item)

    def act_new_tournament_clicked(self):
        if self.dial_new_tournament is None:
            self.dial_new_tournament = ChildNewTournament(self.btn_ok_dial_new_tournament_clicked,
                                                          self.btn_cancel_dial_new_tournament_clicked)
        self.dial_new_tournament.show()

    def act_add_player_clicked(self):

        if self.dial_add_player is None:
            self.dial_add_player = ChildAddPlayer(self.btn_ok_dial_add_player_clicked,
                                                  self.btn_cancel_dial_add_player_clicked)
        try:
            self.dial_add_player.show()
        except RuntimeError:
            self.dial_add_player = ChildAddPlayer(self.btn_ok_dial_add_player_clicked,
                                                  self.btn_cancel_dial_add_player_clicked)
            self.dial_add_player.show()

    def act_list_clicked(self):
        if self.dial_player_list is None:
            self.dial_player_list = ChildPlayerList()
            self.mdiArea.addSubWindow(self.dial_player_list)
            self.set_table_widget(t.all_players, self.dial_player_list.player_list)
        try:
            self.dial_player_list.show()
        except RuntimeError:
            self.dial_player_list = ChildPlayerList()
            self.mdiArea.addSubWindow(self.dial_player_list)
            self.set_table_widget(t.all_players, self.dial_player_list.player_list)
            self.dial_player_list.show()

    def btn_ok_dial_add_player_clicked(self):
        pass

    def btn_cancel_dial_add_player_clicked(self):
        self.dial_add_player.close()

    def btn_ok_dial_new_tournament_clicked(self):
        if self.dial_new_tournament.edit_tournament_name.text() == '':
            print('Type something ...')
        else:
            self.T = mainClasses.Tournament(self.dial_new_tournament.edit_tournament_name.text())
            self.dial_new_tournament.close()

    def btn_cancel_dial_new_tournament_clicked(self):
        self.dial_new_tournament = None


if __name__ == '__main__':
    t = mainClasses.Tournament()
    t.from_xml("xml_file.xml")
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.run()
    # window.add_to_list(t.all_players)
    # window.set_table_widget(t.all_players)
    window.show()
    sys.exit(app.exec_())