import os
from PyQt4 import uic


class CUiCompiler:

    def __init__(self, name_xml_file, name_python_output_file="py_layout"):

        if name_xml_file[-2:] == 'ui':
            self.xml_file_str = name_xml_file
        else:
            self.xml_file_str = name_xml_file + '.ui'

        if name_python_output_file[-2:] == 'py':
            self.xml_file_str = name_python_output_file
        else:
            self.output_file_str = name_python_output_file + '.py'

        self.xml_file_path = os.path.join("", self.xml_file_str)

    def compile(self):
        py_file = open(self.output_file_str, 'w')
        uic.compileUi(self.xml_file_path, py_file)


if __name__ == '__main__':
    CUiCompiler('layout_1_0.ui', 'py_main_ui').compile()
    CUiCompiler('dialog_players', 'py_dialog_players_ui').compile()
    CUiCompiler('dialog_add_player', 'py_dialog_add_player_ui').compile()
    CUiCompiler('dialog_new_tournament', 'py_dialog_new_tournament_ui').compile()
    CUiCompiler('dialog_make_pair', 'py_dialog_make_pair_ui').compile()
