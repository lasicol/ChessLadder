
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

    def setup(self):
        self.mdiArea.setAttribute()


    def run(self):
        self.actionNew_tournament.triggered.connect(self.act_new_tournament_clicked)

    def add_to_list(self, list_of_string):
        for i in list_of_string:
            self.listWidget.addItem(i.str_with_rank())

    def set_table_widget(self, list_):
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'RANK', 'FIRST NAME', 'LAST NAME', 'ELO'])
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        for i, ppl in enumerate(list_):
            self.tableWidget.setItem(i, 0, QtGui.QTableWidgetItem(str(ppl.id)))
            self.tableWidget.setItem(i, 1, QtGui.QTableWidgetItem(str(ppl.rank)))
            self.tableWidget.setItem(i, 2, QtGui.QTableWidgetItem(str(ppl.first_name)))
            self.tableWidget.setItem(i, 3, QtGui.QTableWidgetItem(str(ppl.last_name)))
            self.tableWidget.setItem(i, 4, QtGui.QTableWidgetItem(str(ppl.elo)))
        # item = QtGui.QTableWidgetItem("lody")
        # self.tableWidget.setItem(1,0,item)

    def act_new_tournament_clicked(self):
        # self.subwindows[0].show()
        try:
            self.child.show()
        except RuntimeError:
            self.child = ChildMDI()
            self.mdiArea.addSubWindow(self.child)
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
    window.set_table_widget(t.all_players)
    window.show()
    sys.exit(app.exec_())