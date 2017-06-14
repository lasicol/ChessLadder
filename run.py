import mainClasses
from UI.py_main_ui import Ui_MainWindow
from child_dialogs import *
from PyQt4 import QtGui, QtCore
import sys


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
        self.dial_round = QtGui.QDialog()
        self.dial_input_results = QtGui.QDialog()

        self.dials = [self.dial_player_list,
                      self.dial_add_player,
                      self.dial_new_tournament,
                      self.dial_round]

        # Tournament
        self.isTournament = False
        self.T = None
        self.opened_file = ""

        # Toolbar actions:
        self.act_add_player = QtGui.QIcon()
        self.act_list = QtGui.QIcon()
        self.act_sort = QtGui.QIcon()
        self.act_make_pair = QtGui.QIcon()
        self.act_round = QtGui.QIcon()
        self.act_input_results = QtGui.QIcon()

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

        if self.T is not None:
            if self.T.round > 0:
                self.act_sort.setEnabled(False)

    # noinspection PyBroadException
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
        QtGui.QAction.connect(self.act_add_player, QtCore.SIGNAL('triggered()'), self.act_add_player_clicked)

        # List
        self.act_list = QtGui.QAction(QtGui.QIcon("Graph\icList.png"), "show list", self)
        self.toolBar.addAction(self.act_list)
        QtGui.QAction.connect(self.act_list, QtCore.SIGNAL('triggered()'), self.act_list_clicked)

        # Sort
        self.act_sort = QtGui.QAction(QtGui.QIcon("Graph\icSort.png"), "sort list by rank", self)
        self.toolBar.addAction(self.act_sort)
        QtGui.QAction.connect(self.act_sort, QtCore.SIGNAL('triggered()'), self.act_sort_clicked)

        # Make pair
        self.act_make_pair = QtGui.QAction(QtGui.QIcon("Graph\icHandshake.png"), "make a pair", self)
        self.toolBar.addAction(self.act_make_pair)
        QtGui.QAction.connect(self.act_make_pair, QtCore.SIGNAL('triggered()'), self.act_make_pair_clicked)

        # Show pairs
        self.act_round = QtGui.QAction(QtGui.QIcon("Graph\icPair.png"), "round", self)
        self.toolBar.addAction(self.act_round)
        QtGui.QAction.connect(self.act_round, QtCore.SIGNAL('triggered()'), self.act_round_clicked)

        # Input results
        self.act_input_results = QtGui.QAction(QtGui.QIcon("Graph\icNotebook.png"), "Input results", self)
        self.toolBar.addAction(self.act_input_results)
        QtGui.QAction.connect(self.act_input_results, QtCore.SIGNAL('triggered()'), self.act_input_results_clicked)

    def add_to_list(self, list_of_string):
        for i in list_of_string:
            self.listWidget.addItem(i.str_with_rank())

    @staticmethod
    def set_list_table_widget(list_, table_widget):
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

    def set_round_table_widget(self, list_, table_widget):
        table_widget.setRowCount(len(list_))
        table_widget.setColumnCount(3)

        table_widget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        for i, ppl in enumerate(list_):
            if isinstance(list_[i], list):
                table_widget.setItem(i, 0, QtGui.QTableWidgetItem(str(self.T.get_player_by_id(list_[i][0]))))
                if self.T.results[self.T.round-1][i] == -1:
                    table_widget.setItem(i, 1, QtGui.QTableWidgetItem("-:-"))
                elif self.T.results[self.T.round-1][i] == 1:
                    table_widget.setItem(i, 1, QtGui.QTableWidgetItem("1-0"))
                elif self.T.results[self.T.round-1][i] == 2:
                    table_widget.setItem(i, 1, QtGui.QTableWidgetItem("0.5-0.5"))
                elif self.T.results[self.T.round-1][i] == 0:
                    table_widget.setItem(i, 1, QtGui.QTableWidgetItem("0-1"))
                table_widget.setItem(i, 2, QtGui.QTableWidgetItem(str(self.T.get_player_by_id(list_[i][1]))))
            else:
                table_widget.setItem(i, 0, QtGui.QTableWidgetItem(str(self.T.get_player_by_id(list_[i]))))


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
                self.set_list_table_widget(self.T.all_players, self.dial_player_list.player_list)
        try:
            self.dial_player_list.showMaximized()
        except RuntimeError:
            self.dial_player_list = ChildPlayerList()
            self.mdiArea.addSubWindow(self.dial_player_list)
            # self.dial_player_list.setWindowState(QtCore.Qt.WindowMaximized)
            if self.T is not None:
                self.set_list_table_widget(self.T.all_players, self.dial_player_list.player_list)
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
            self.set_list_table_widget(self.T.all_players, self.dial_player_list.player_list)

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
        [print(hex(id(i.list_of_opponents))) for i in self.T.all_players]
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
        self.T.make_pair(self.T.present_players)

        self.act_round_clicked()
        self.dial_make_pair.close()
        self.update()


    def btn_cancel_dial_make_pair_clicked(self):
        pass

    def btn_ok_dial_input_results_clicked(self):
        print(self.dial_input_results.results)
        results = self.dial_input_results.results[:len(self.T.paired)]
        print(results)
        if len(self.T.results) < self.T.round:
            self.T.results.append(results)
        else:
            self.T.results.pop(self.T.round-1)
            self.T.results.insert(self.T.round-1, results)

        for i, result in enumerate(self.T.results[self.T.round-1]):
            if isinstance(self.T.paired[i], list):
                ppl1 = self.T.get_player_by_id(self.T.paired[i][0])
                ppl2 = self.T.get_player_by_id(self.T.paired[i][1])
                if result == 1:
                    if ppl1.rank > ppl2.rank:
                        ppl1.rank, ppl2.rank = ppl2.rank, ppl1.rank
                    else:
                        pass
                elif result == 2:
                    pass
                elif result == 0:
                    if ppl1.rank < ppl2.rank:
                        ppl1.rank, ppl2.rank = ppl2.rank, ppl1.rank
                    else:
                        pass
        self.T.all_players = self.T.sort_by_rank(self.T.all_players)
        [print(x.rank) for x in self.T.all_players]

    def btn_cancel_dial_input_results_clicked(self):
            pass

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
        self.T.all_players = self.T.sort_by_elo(self.T.all_players)
        self.T.set_rank()
        if self.dial_player_list is not None:
            self.set_list_table_widget(self.T.all_players, self.dial_player_list.player_list)

    def act_make_pair_clicked(self):
        self.dial_make_pair = ChildMakePair(self.btn_ok_dial_make_pair_clicked, self.btn_cancel_dial_make_pair_clicked)
        for i in self.T.all_players:
            self.dial_make_pair.listWidget_all.addItem(str(i))
        self.dial_make_pair.num_round.setValue(self.T.round + 1)
        self.dial_make_pair.show()

    def     act_round_clicked(self):
        if self.dial_round is not ChildRound:
            self.dial_round = ChildRound()
            self.mdiArea.addSubWindow(self.dial_round)
            self.set_round_table_widget(self.T.paired, self.dial_round.table_paired_players)
        self.dial_round.showMaximized()

    def act_input_results_clicked(self):
        self.dial_input_results = ChildInputResults(self.btn_ok_dial_input_results_clicked,
                                                    self.btn_cancel_dial_input_results_clicked)
        self.dial_input_results.show()
        self.set_round_table_widget(self.T.paired, self.dial_input_results.table_paired_players_input)


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
