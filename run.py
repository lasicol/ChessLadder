import mainClasses
from UI.py_main_ui import Ui_MainWindow
from UI.py_dialog_players_ui import Ui_dial_list
from UI.py_dialog_add_player_ui import Ui_dial_add_player
from UI.py_dialog_new_tournament_ui import Ui_dial_new_tournament
from UI.py_dialog_make_pair_ui import Ui_dial_make_pair
from PyQt4 import QtGui, Qt, QtCore
import sys


class ChildPlayerList(QtGui.QDialog, Ui_dial_list):
    def __init__(self):
        super(ChildPlayerList, self).__init__(None)
        self.setupUi(self)

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
            item = None # remove from listWidget_all

    def btn_move_left_clicked(self):
        item = self.listWidget_selected.takeItem(self.listWidget_selected.currentRow())
        if item is not None:
            self.listWidget_all.addItem(item.text())
            item = None # remove from listWidget_all

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Dialogs
        self.dial_player_list = None
        self.dial_add_player = None
        self.dial_new_tournament = None
        self.dial_make_pair = QtGui.QDialog()
        self.dials = [self.dial_player_list,
                      self.dial_add_player,
                      self.dial_new_tournament]

        # Tournament
        self.isTournament = False
        self.T = None
        self.opened_file = ""

        # Toolbar actions:
        self.act_add_player = QtGui.QIcon()
        self.act_list = QtGui.QIcon()
        self.act_sort = QtGui.QIcon()
        self.act_make_pair = QtGui.QIcon()

        self.setup()
        self.update()

    def setup(self):
        self.set_toolbar()

        self.actionNew_tournament.triggered.connect(self.act_new_tournament_clicked)
        self.actionOpen.triggered.connect(self.act_open_clicked)
        self.actionSave.triggered.connect(self.act_save_clicked)

    def update(self):
        if self.isTournament:
            self.toolBar.setEnabled(True)
            self.actionSave.setEnabled(True)
        else:
            self.toolBar.setDisabled(True)
            self.actionSave.setDisabled(True)

        self.dials = [self.dial_player_list,
                      self.dial_add_player,
                      self.dial_new_tournament]

    def close_all_dial_and_clear(self):
        for i in self.dials:
            if i is not None:
                try:
                    i.close()
                except:
                    pass

    def run(self):
        pass

    def set_toolbar(self):
        # Add player
        self.act_add_player = QtGui.QAction(QtGui.QIcon("Graph\icAddUser.png"), "new user", self)
        self.toolBar.addAction(self.act_add_player)
        self.act_add_player.triggered.connect(self.act_add_player_clicked)

        # List
        self.act_list = QtGui.QAction(QtGui.QIcon("Graph\icList.png"), "show list", self)
        self.toolBar.addAction(self.act_list)
        self.act_list.triggered.connect(self.act_list_clicked)

        #Sort
        self.act_sort = QtGui.QAction(QtGui.QIcon("Graph\icSort.png"), "sort list by rank", self)
        self.toolBar.addAction(self.act_sort)
        self.act_sort.triggered.connect(self.act_sort_clicked)

        # Make pair
        self.act_make_pair = QtGui.QAction(QtGui.QIcon("Graph\icHandshake.png"), "make a pair", self)
        self.toolBar.addAction(self.act_make_pair)
        self.act_make_pair.triggered.connect(self.act_make_pair_clicked)

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
            self.dial_add_player = ChildAddPlayer(self.btn_add_dial_add_player_clicked,
                                                  self.btn_ok_dial_add_player_clicked)
        try:
            self.dial_add_player.show()
        except RuntimeError:
            self.dial_add_player = ChildAddPlayer(self.btn_add_dial_add_player_clicked,
                                                  self.btn_ok_dial_add_player_clicked)
            self.dial_add_player.show()

    def act_list_clicked(self):
        if self.dial_player_list is None:
            self.dial_player_list = ChildPlayerList()
            self.mdiArea.addSubWindow(self.dial_player_list)
            if self.T is not None:
                self.set_table_widget(self.T.all_players, self.dial_player_list.player_list)
        try:
            self.dial_player_list.showMaximized()
        except RuntimeError:
            self.dial_player_list = ChildPlayerList()
            self.mdiArea.addSubWindow(self.dial_player_list)
            # self.dial_player_list.setWindowState(QtCore.Qt.WindowMaximized)
            if self.T is not None:
                self.set_table_widget(self.T.all_players, self.dial_player_list.player_list)
            self.dial_player_list.showMaximized()

    def btn_add_dial_add_player_clicked(self):
        first = self.dial_add_player.edit_first.text()
        last = self.dial_add_player.edit_last.text()
        try:
            elo = int(self.dial_add_player.edit_elo.text())
        except ValueError:
            return

        if not (first == '' or last == '' or elo > 3000):
            self.T.add_player(first, last, elo)
            self.dial_add_player.edit_first.setText('')
            self.dial_add_player.edit_last.setText('')
            self.dial_add_player.edit_elo.setText('')
            self.dial_add_player.label_status.setText('Added correctly.')
            self.update()

        if self.dial_player_list is not None:
            self.set_table_widget(self.T.all_players, self.dial_player_list.player_list)

    def btn_ok_dial_add_player_clicked(self):
        self.dial_add_player.close()
        self.update()

    def btn_ok_dial_new_tournament_clicked(self):
        if self.dial_new_tournament.edit_tournament_name.text() == '':
            print('Type something ...')
        else:
            self.T = mainClasses.Tournament(self.dial_new_tournament.edit_tournament_name.text())
            self.isTournament = True
            self.update()
            self.close_all_dial_and_clear()
        self.update()

    def btn_cancel_dial_new_tournament_clicked(self):
        self.dial_new_tournament = None
        self.update()

    def btn_ok_dial_make_pair_clicked(self):
        items = []
        for index in range(self.dial_make_pair.listWidget_selected.count()):
            items.append(self.dial_make_pair.listWidget_selected.item(index).text())

        selected_players = []
        for i in items:
            splitted = i.split('.')
            player_id = splitted[0]
            ppl = self.T.get_player_by_id(player_id)
            if ppl:
                selected_players.append(self.T.get_player_by_id(player_id))
        self.T.present_players = self.T.sort_by_rank(selected_players)

        # [print(x) for x in self.T.present_players]


    def btn_cancel_dial_make_pair_clicked(self):
        pass

    def btn_cancel_dial_new_tournament_clicked(self):
        self.dial_new_tournament = None
        self.update()


    def act_open_clicked(self):
        self.opened_file = QtGui.QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Xml file(*.xml)")
        if self.opened_file:
            self.T = mainClasses.Tournament()
            if self.T.from_xml(self.opened_file):
                print("success")
                self.isTournament = True
            else:
                print("can't open this file...")
            self.update()

    def act_save_clicked(self):
        if self.isTournament:
            file_name = QtGui.QFileDialog.getSaveFileName(self, 'Dialog Title', 'c:\\', '*.xml')
            if file_name:
                self.T.to_xml(file_name)
        self.update()

    def act_sort_clicked(self):
        self.T.all_players = self.T.sort_by_rank(self.T.all_players)
        self.T.set_rank()
        if self.dial_player_list is not None:
            self.set_table_widget(self.T.all_players, self.dial_player_list.player_list)

    def act_make_pair_clicked(self):
        self.dial_make_pair = ChildMakePair(self.btn_ok_dial_make_pair_clicked, self.btn_cancel_dial_make_pair_clicked)
        for i in self.T.all_players:
            self.dial_make_pair.listWidget_all.addItem(str(i))
        self.dial_make_pair.show()

if __name__ == '__main__':
    # t = mainClasses.Tournament()
    # t.from_xml("xml_file.xml")
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.run()
    # window.add_to_list(t.all_players)
    # window.set_table_widget(t.all_players)
    window.show()
    sys.exit(app.exec_())
