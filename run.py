
import mainClasses
from UI.py_main_ui import Ui_MainWindow
from UI.py_dialog_ui import Ui_dialog_add
from PyQt4 import QtGui
import sys


class ChildMDI(QtGui.QDialog, Ui_dialog_add):
    def __init__(self):
        super(ChildMDI, self).__init__(None)
        self.setupUi(self)


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.child = ChildMDI()

        self.mdiArea.addSubWindow(self.child)

        self.subwindows = self.mdiArea.subWindowList()
        self.subwindows[0].hide()
        self.subwindows[0].show()
        self.set_toolbar()

    def setup(self):
        self.mdiArea.setAttribute()


    def run(self):
        self.actionNew_tournament.triggered.connect(self.act_new_tournament_clicked)

    def set_toolbar(self):
        act_add_user = QtGui.QAction(QtGui.QIcon("Graph\icAddUser.png"), "new user", self)
        self.toolBar.addAction(act_add_user)

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
        # self.subwindows[0].show()
        try:
            self.child.show()
        except RuntimeError:
            self.child = ChildMDI()
            self.mdiArea.addSubWindow(self.child)
            self.set_table_widget(t.all_players, self.child.player_list)
            self.child.show()

        # self.mdiArea.addSubWindow(self.child)
        # sub = self.mdiArea.subWindowList()
        # sub[0].show()
        # for i in sub:
        #     if i.isEnable():
        #         print("lol")



        # self.subwindows[0].show()

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