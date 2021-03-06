import xml.etree.ElementTree as ET
import os
from random import randint

PROMOTE = 1
DEFEND = 2
WHITE = 1
BLACK = 2

class Player:
    """" The class which is describing player object"""
    id = 0

    def __init__(self, first_name, last_name, elo, rank=0, p_id=0, last_opponent=0, list_of_opponents=None,
                 last_game=None):
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
        self.last_game = last_game

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
        self.paired = []
        self.results = []

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
    def sort_by_elo(p_list):
        return sorted(p_list, key=lambda x: x.elo, reverse=True)

    @staticmethod
    def sort_by_rank(p_list):
        return sorted(p_list, key=lambda x: x.rank)

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

    def _swap(self, ppl1, ppl2):
        print(ppl1, ppl2)
        ranks = range(ppl1.rank-1, ppl2.rank-1)
        print(ranks)
        ppl2.rank = ppl1.rank
        for i in ranks:
            self.all_players[i].rank += 1
        self.all_players = self.sort_by_rank(self.all_players)


    def _punishment(self, selected_players):
        ppl1 = None
        ppl2 = None
        flag = True
        for i, ppl in enumerate(self.all_players):
            if ppl not in selected_players and flag:
                ppl1 = ppl
                flag = False
            elif ppl in selected_players:
                if not flag:
                    ppl2 = ppl
                    flag = True
                    self._swap(ppl1, ppl2)

    def pair1(self, selected_players: list()):
        defenders = []
        promoters = []
        paired = []
        for ppl in selected_players:
            if ppl.last_game is not None:
                if ppl.last_game.kind_of == DEFEND:
                    promoters.append(ppl)
                elif ppl.last_game.kind_of == PROMOTE:
                    defenders.append(ppl)
            else:
                promoters.append(ppl)

        for ppl_promoter in promoters:
            for ppl_defender in defenders:
                diff = ppl_promoter.rank - ppl_defender.rank
                if ppl_promoter.id != ppl_defender.last_game.opponent.id and diff > 0:
                    paired.append([ppl_promoter.id, ppl_defender.id])
                    promoters.remove(ppl_promoter)
                    defenders.remove(ppl_defender)
                    break

        return paired

    def pair2(self, selected_players):
        paired = []
        copy_selected = list(selected_players)
        done = False

        while not done:
            for i, ppl in enumerate(copy_selected):
                max_value = len(copy_selected) - i - 1
                if max_value == 1:
                    if copy_selected[i+1] == ppl.last_game.opponent:
                        done = True
                        break
                    else:
                        paired.append([copy_selected[i + 1].id, ppl.id])
                        copy_selected.remove(copy_selected[i + 1])
                        copy_selected.remove(ppl)
                        done = True
                        break
                elif max_value < 1:
                    done = True
                    break

                if max_value > 3:
                    max_value = 3
                rand = randint(1, max_value)

                while copy_selected[i+rand] == ppl.last_game.opponent:
                    rand = randint(1, max_value)

                paired.append([copy_selected[i+rand].id, ppl.id])
                copy_selected.remove(copy_selected[i + rand])
                copy_selected.remove(ppl)
                break

        return paired

    def count_not_paired(self, selected_players, paired):
        players_left = list(selected_players)
        count = 0
        for ppl in players_left:
            for paired_ppl in paired:
                if ppl.id in paired_ppl:
                    count += 1
        return len(players_left) - count

    def make_pair(self, selected_players: list()):
        self.paired = []
        self._punishment(selected_players)

        if self.round == 1:
            for i in range(0, len(selected_players), 2):
                try:
                    self.paired.append([selected_players[i+1].id, selected_players[i].id])
                except:
                    pass
        else:
            paired1 = self.pair1(selected_players)
            paired2 = self.pair2(selected_players)
            paired1_count = self.count_not_paired(selected_players, paired1)
            paired2_count = self.count_not_paired(selected_players, paired2)

            print("Piared1: {}, paired2: {}".format(paired1_count, paired2_count))

            if paired1_count > paired2_count:
                self.paired = paired2
            else:
                self.paired = paired1

        for pairs in self.paired:
            if isinstance(pairs, list):
                ppl1 = self.get_player_by_id(pairs[0])
                ppl2 = self.get_player_by_id(pairs[1])

                ppl1.last_game = Game(PROMOTE, ppl2)
                ppl2.last_game = Game(DEFEND, ppl1)

            else:
                pass

        print(self.paired)
        # print(players_left)
        self.results.append([-1] * (len(self.paired)))

        # white = []
        # black = []
        # self.paired = []
        # size_selected_player = len(selected_players)
        # copy_list = list(selected_players)
        # while 1:
        #     if len(copy_list) == 0:
        #         break
        #     ppl_1 = copy_list[0]
        #     i = 0
        #     for p in copy_list[1:]:
        #         if p.list_of_opponents[-1] != ppl_1.id or p.list_of_opponents[-1] == 0:
        #             org_player1 = self.get_player_by_id(ppl_1.id)
        #             org_player2 = self.get_player_by_id(p.id)
        #             if org_player1 and org_player2:
        #                 org_player1.add_opponent(org_player2.id)
        #                 org_player2.add_opponent(org_player1.id)
        #                 self.paired.append([org_player1.id, org_player2.id])
        #             copy_list.remove(ppl_1)
        #             copy_list.remove(p)
        #             break
        #         if i == 2:
        #             break
        #         i += 1
        #     # [print(i) for i in copy_list]
        #     # print('------------------')
        #     print(self.paired)
        #     if len(copy_list) == size_selected_player:
        #         break
        #     else:
        #         size_selected_player = len(copy_list)
        #
        # self.round += 1
        #
        # [self.paired.append(i.id) for i in copy_list]
        # print(self.paired)
        # self.results.append([-1]*(len(self.paired)))

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


class Game:

    def __init__(self, kind_of, opponent: Player):

        self.kind_of = kind_of
        self.opponent = opponent
        if self.kind_of == PROMOTE:
            self.colour = WHITE
        else:
            self.colour = BLACK



if __name__ == "__main__":
    t = Tournament()
    # t.import_player_list_from_file("test.txt")
    # t.sort_by_rank(t.all_players)
    # t.set_a_rank(t.all_players)
    # t.to_xml("xml_file.xml")
    t.from_xml("xml_file.xml")
    # t.prepare_to_fight()