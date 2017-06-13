import xml.etree.ElementTree as ET
import os


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
        self.last_colour = ""
        if list_of_opponents is None:
            self.list_of_opponents = [0]
        else:
            self.list_of_opponents = list_of_opponents

    def add_opponent(self, pid):
        self.list_of_opponents.append(pid)

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
    def __init__(self, name='Example of tournament', current_round=0):
        self.name = name
        self.all_players = []
        self.present_players = []
        self.round = current_round

    def add_player(self, first, last, elo):
        id_p = len(self.all_players)+1
        self.all_players.append(Player(first, last, elo, p_id=id_p))

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

    @staticmethod
    def sort_by_rank(p_list):
        return sorted(p_list, key=lambda x: x.elo, reverse=True)

    @staticmethod
    def sort_by_id(players):
        return sorted(players, key=lambda player: player.id)

    @staticmethod
    def print_players(players):
        [print(player) for player in players]

    def set_rank(self):
        for i, player in enumerate(self.all_players):
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
        try:
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
            return True
        except:
            return False

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

    def make_pair(self, selected_players: list()):

        white = []
        black = []
        paired = []
        size_selected_player = len(selected_players)
        copy_list = list(selected_players)
        while 1:
            ppl_1 = copy_list[0]
            for p in copy_list[1:]:
                if p.list_of_opponents[0] != ppl_1.list_of_opponents[0] or p.list_of_opponents[0] == 0:
                    org_player1 = self.get_player_by_id(ppl_1.id)
                    org_player2 = self.get_player_by_id(p.id)
                    if org_player1 and org_player2:
                        org_player1.add_opponent(org_player2.id)
                        org_player2.add_opponent(org_player1.id)
                        paired.append([org_player1.id, org_player2.id])
                    copy_list.remove(ppl_1)
                    copy_list.remove(p)
                    break
            # [print(i) for i in copy_list]
            # print('------------------')
            print(paired)
            if len(copy_list) == size_selected_player:
                break
            else:
                size_selected_player = len(copy_list)
        return paired

    def get_player_by_id(self, pid):
        ppl = None
        if type(pid) is int:
            for player in self.all_players:
                if player.id == pid:
                    ppl = player
                    break
        else:
            for player in self.all_players:
                if str(player.id) == pid:
                    ppl = player
                    break
        if ppl is None:
            return False
        else:
            return ppl

if __name__ == "__main__":
    t = Tournament()
    # t.import_player_list_from_file("test.txt")
    # t.sort_by_rank(t.all_players)
    # t.set_a_rank(t.all_players)
    # t.to_xml("xml_file.xml")
    t.from_xml("xml_file.xml")
    # t.prepare_to_fight()