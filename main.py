import xml.etree.ElementTree as ET
import os
import sys
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "UI\layout_1_0.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class Player:
    """" The class which is describing player object"""
    id = 0

    def __init__(self, first_name, last_name, elo, rank=0, p_id=0, last_opponent=0, list_of_opponents=None):
        self.first_name = first_name
        self.last_name = last_name
        self.elo = int(elo)
        self.rank = rank
        Player.id += 1
        if not p_id:
            self.id = Player.id
        else:
            self.id = p_id
        self.last_opponent = last_opponent
        self.list_of_opponents = list_of_opponents

    def __str__(self):
        return str(self.id) + ".   " + self.first_name + ", " + self.last_name + ", " + str(self.elo)

    def str_with_rank(self):
        return str(self.rank) + ".   " + self.first_name + ", " + self.last_name + ", " + str(self.elo)

    def to_xml(self, xml_object):
        first_name = ET.SubElement(xml_object, 'first_name')
        first_name.text = self.first_name
        last_name = ET.SubElement(xml_object, 'last_name')
        last_name.text = self.last_name
        elo = ET.SubElement(xml_object, 'elo')
        elo.text = str(self.elo)
        id_xml = ET.SubElement(xml_object, 'id')
        id_xml.text = str(self.id)
        rank = ET.SubElement(xml_object, 'rank')
        rank.text = str(self.rank)
        l_opp = ET.SubElement(xml_object, 'last_opponent')
        l_opp.text = str(self.last_opponent)


class Tournament:
    def __init__(self, name='Example of tournament', current_round=0, all_players=None):
        print("You have just created new tournament: " + name)
        self.name = name
        self.all_players = all_players
        self.present_players = []
        self.round = current_round

    def import_player_list_from_file(self, file_path):
        f = open(file_path, 'r')
        for i in f:
            str_data = i.split(sep=';')
            fname = str_data[0]
            lname = str_data[1]
            elo = str_data[2]
            self.all_players.append(Player(fname, lname, elo))
        f.close()

    def delete_all_players(self):
        self.all_players = []

    def sort_by_rank(self, players):
        return sorted(players, key=lambda player: player.elo).reverse()

    def sort_by_id(self, players):
        return sorted(players, key=lambda player: player.id)

    def print_players(self, players):
        [print(player) for player in players]

    def set_a_rank(self, players_list):
        for i, player in enumerate(players_list):
            player.rank = i + 1

    def to_xml(self, xml_file_path):
        tournament = ET.Element('tournament')

        name = ET.SubElement(tournament, 'name')
        name.text = self.name
        current_round = ET.SubElement(tournament, 'round')
        current_round.text = str(self.round)

        players = ET.SubElement(tournament, 'players')
        for i in self.all_players:
            player_id = ET.SubElement(players, "Player")
            i.to_xml(player_id)
        tree = ET.ElementTree(tournament)
        tree.write(xml_file_path)

    def from_xml(self, xml_file_path):
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        self.name = root.find("name").text
        self.round = int(root.find("round").text)
        pl = root.find('players')
        for i in pl.findall("Player"):
            self.all_players.append(Player(first_name=i.find("first_name").text,
                                           last_name=i.find("last_name").text,
                                           elo=int(i.find("elo").text),
                                           rank=int(i.find("rank").text),
                                           p_id=int(i.find("id").text),
                                           last_opponent=int(i.find("last_opponent").text)))

        self.print_players(self.all_players)

    def prepare_to_fight(self):
        self.present_players = self.all_players
        id_list = [p.id for p in self.present_players]
        clear = lambda: os.system('cls')
        clear()
        while True:
            print("Which player is absent?")
            self.print_players(self.sort_by_id(self.present_players))
            a = input("Type id of absent player and hit enter. [Type 'Confirm' when done]: ")
            if a == 'Confirm':
                break
            else:
                try:
                    a = int(a)
                except ValueError:
                    print("You have to chose an ID!!")
            print(a in id_list)
            if a in id_list:
                print(a in id_list)
                id_list.remove(a)
                for i in self.present_players:
                    if i.id == a:
                        self.present_players.remove(i)
            else:
                print("There is no such an id...")
            print("=============================================================")

    def make_pair(self):

        pass


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.mdiArea.addSubWindow(self.subwindow)

    def run(self):
        self.actionNew_tournament.triggered.connect(self.act_new_tourn_Clicked)

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
        self.mdiArea.addSubWindow(self.subwindow)


def main():
    t = Tournament()
    # t.import_player_list_from_file("test.txt")
    # t.sort_by_rank(t.all_players)
    # t.set_a_rank(t.all_players)
    # t.to_xml("xml_file.xml")
    t.from_xml("xml_file.xml")
    # t.prepare_to_fight()

    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.run()
    # window.add_to_list(t.all_players)
    window.set_tableWidget(t.all_players)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()