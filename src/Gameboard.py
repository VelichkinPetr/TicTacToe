from __future__ import annotations
from customtkinter import *

from src.Cell import Cell


class GameBoard:


    def __init__(self, root: CTk, judge, players: list):
        self.__root = root
        self.__judge = judge
        self.__players = players or []
        self.__viewer = GameBoardViewer(root, self.__players)
        self.__model = GameBoardModel(self.__viewer.board_cells)


    def get_cells(self):
        return self.__model.get_cells()

    def get_board_str(self):
        return self.__model.get_matrix_str()

    def __registration_events_bottons_gameboard(self, mode: int, difficulty: str) -> None:

        for cells in self.__viewer.board_cells:
            for cell in cells:
                cell.add_handler_on_click(lambda cell = cell :self.__handler_on_click(cell, mode, difficulty))
        self.__viewer.add_handler_back(self.__handler_on_click_back)

    def __handler_on_click(self, cell: Cell, mode: int, difficulty: str) -> None:

        if mode == 1:
            self.__judge.game_with_pc(self.__players[0], self.__players[2], cell, self, difficulty)
        if mode == 2:
            self.__judge.game_with_player(self.__players[1], self.__players[2], cell, self)

    def __handler_on_click_back(self) -> None:
        self.__judge.set_steps_null()
        self.__viewer.frame_gameboard.destroy()
        self.__menu_mode.draw()

    def draw(self, mode: int, difficulty: str) -> None:
        '''

        :param mode: 1 - одиночная игра, 2 - с другом
        :param difficulty: сложность
        :return:
        '''
        self.__viewer.create_widgets(mode, self.__viewer.board_cells)
        self.__registration_events_bottons_gameboard(mode, difficulty)

    def add_reaction_on_back(self, menu_mode) -> None:
        self.__menu_mode = menu_mode

    def clear(self):
        self.__model.clear()
        self.__viewer.clear()

    def change_player(self):
        self.__viewer.change_player()

    def do_sleep(self,func):
        self.__viewer.do_sleep(func)



class GameBoardViewer:


    def __init__(self, root: CTk, players: list):
        self.__root = root
        self.frame_gameboard = self.__create_frame()
        self.players = players
        self.board_cells = self.__create_cells()


    def __create_cells(self) -> list[list[Cell]]:

        matrix_cell = []
        for i in range(0, 3):
            row = []
            for k in range(0, 3):
                c = Cell(self.frame_gameboard,i, k)
                row.append(c)
            matrix_cell.append(row)
        return matrix_cell

    def __create_frame(self) -> CTkFrame:

        frame = CTkFrame(self.__root, height=300, width=350)
        frame.grid(row=0, column=0)
        return frame

    def __create_botton(self, color: str, text: str) -> CTkButton:
        return CTkButton(self.frame_gameboard, text= text, height=20, width=150, fg_color=color,
                         border_color='black', text_color='black')

    def __create_players(self, mode: int) -> None:

        if mode == 2:
            self.btn_player1 = self.__create_botton('#66CD00', self.players[2].get_name() + ":" +  self.players[2].get_side())
            self.btn_player1.grid(row=4, column=0)

            self.btn_player2 = self.__create_botton('#CD3333', self.players[1].get_name() + " : " +  self.players[1].get_side())
            self.btn_player2.grid(row=4, column=2)

        else:
            self.btn_player1 = self.__create_botton('#66CD00', self.players[2].get_name() + " : " +  self.players[2].get_side())
            self.btn_player1.grid(row=4, column=0)

            self.btn_player2 = self.__create_botton('#CD3333',self.players[0].get_name() + " : " +  self.players[0].get_side())
            self.btn_player2.grid(row=4, column=2)

    def create_widgets(self, mode: int, board: list[list[Cell]]) -> None:
        for i in board:
            for n in i:
                n.create_cell()

        self.__create_players(mode)

        self.btn_back = self.__create_botton('grey', 'back')
        self.btn_back.grid(row=4, column=1)

    def add_handler_back(self,handler) -> None:
        self.btn_back.configure(command=handler)

    def do_sleep(self, func):
        self.frame_gameboard.after(100, func)

    def clear(self) -> None:
        self.btn_player1.configure(state=NORMAL, fg_color='#66CD00')
        self.btn_player2.configure(state=DISABLED, fg_color='#CD3333')

    def change_player(self) -> None:

        if self.btn_player1.cget('fg_color') == '#66CD00':
            self.btn_player1.configure(state=DISABLED, fg_color='#CD3333')
            self.btn_player2.configure(state=NORMAL, fg_color='#66CD00')
        else:
            self.btn_player1.configure(state=NORMAL, fg_color='#66CD00')
            self.btn_player2.configure(state=DISABLED, fg_color='#CD3333')



class GameBoardModel:


    def __init__(self, board_cells):
        self.__board = board_cells


    def get_cells(self) -> list[list[Cell]]:
        return self.__board

    def get_matrix_str(self) -> list[list[str]]:
        matrix_str = []
        for cells in self.__board:
            row = []
            for cell in cells:
                row.append(cell.get_value())
            matrix_str.append(row)

        return matrix_str

    def clear(self) -> None:

        for i in self.__board:
            for n in i:
                n.clear()