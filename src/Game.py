from __future__ import annotations
import customtkinter
from customtkinter import *

import config
from src.Menu import Menu
from src.Gameboard import GameBoard
from src.Judge import Judge
from src.User import User



class Game:

    def __init__(self):
        self.__root = self.__create_window()
        self.__menu = Menu(self.__root, self)
        self.__judge = Judge()
        self.__player_1 = User.create(1, 'Gamer 1', 'X')
        self.__player_2 = User.create(1, 'Gamer 2', 'O')
        self.__bot = User.create(2, 'Bot', 'O')


    def __create_window(self) -> CTk:
        window = CTk()
        window.title("X and 0")
        window.grid_columnconfigure(0, weight=1)
        window.grid_rowconfigure(0, weight=1)
        window.resizable(False,False)
        customtkinter.set_default_color_theme(config.THEME_FILE)
        return window

    def run(self) -> None:
        self.__menu.draw()
        self.__root.mainloop()

    def create_session(self, mode: int, difficulty: str, menu_mode) -> None:
        gameboard = GameBoard(self.__root, self.__judge, [self.__bot, self.__player_2, self.__player_1])
        gameboard.add_reaction_on_back(menu_mode)
        gameboard.draw(mode, difficulty)