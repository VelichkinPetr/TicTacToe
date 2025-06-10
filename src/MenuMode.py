from __future__ import annotations
from PIL import Image
from customtkinter import *

import config



class MenuMode:


    def __init__(self, root: CTk, menu, game):
        self.__root = root
        self.__viewer = MenuModeViewer(self.__root)
        self.__game = game
        self.__menu = menu


    def __registration_events_bottons_menu(self) -> None:
        self.__viewer.add_handler_single(self.__handler_on_click_single)
        self.__viewer.add_handler_multi(self.__handler_on_click_multi)
        self.__viewer.add_handler_back(self.__handler_on_click_back)

    def __registration_events_bottons_difficulty(self) -> None:
        self.__viewer.add_handler_easy(self.__handler_on_click_easy)
        self.__viewer.add_handler_medium(self.__handler_on_click_medium)
        self.__viewer.add_handler_hard(self.__handler_on_click_hard)

    def __handler_on_click(self, mode: int, difficulty: str) -> None:
        self.__viewer.clear_menu_mode()
        self.__game.create_session(mode, difficulty ,self)

    def __handler_on_click_single(self) -> None:
        self.__viewer.create_difficulty_widgets()
        self.__registration_events_bottons_difficulty()

    def __handler_on_click_easy(self) -> None:
        self.__handler_on_click(1,'easy')

    def __handler_on_click_medium(self) -> None:
        self.__handler_on_click(1,'medium')

    def __handler_on_click_hard(self) -> None:
        self.__handler_on_click(1,'hard')

    def __handler_on_click_multi(self) -> None:
        self.__handler_on_click(2,'')

    def __handler_on_click_back(self) -> None:
        self.__viewer.clear_menu_mode()
        self.__menu.draw()

    def draw(self) -> None:
        self.__viewer.create_widgets()
        self.__registration_events_bottons_menu()



class MenuModeViewer:


    def __init__(self, root: CTk):
        self.root_window = root
        self.image_easy = CTkImage(light_image=Image.open(config.IMAGE_EASY), size=(40, 40))
        self.image_medium = CTkImage(light_image=Image.open(config.IMAGE_MEDIUM), size=(40, 40))
        self.image_hard = CTkImage(light_image=Image.open(config.IMAGE_HARD), size=(40, 40))


    def __create_botton(self, frame: CTkFrame, text: str, width: int) -> CTkButton:
        return CTkButton(frame, text= text, height=50, width=width)

    def clear_menu_mode(self) -> None:
        self.__frame_menu_mode.destroy()

    def create_difficulty_widgets(self) -> None:

        label_difficulty = CTkLabel(self.__frame_menu_mode, text="---Change Difficulty---")
        label_difficulty.grid(row=0, column=2, columnspan=3)

        self.btn_easy = CTkButton(self.__frame_menu_mode, image=self.image_easy, text="", width=50, height=50, fg_color = ("#D3CFFC", "#5D3A4A"))
        self.btn_easy.grid(row=1, column=2)

        self.btn_medium = CTkButton(self.__frame_menu_mode, image=self.image_medium, text="", width=50, height=50, fg_color = ("#D3CFFC", "#5D3A4A"))
        self.btn_medium.grid(row=1, column=3)

        self.btn_hard = CTkButton(self.__frame_menu_mode, image=self.image_hard, text="", width=50, height=50, fg_color = ("#D3CFFC", "#5D3A4A"))
        self.btn_hard.grid(row=1, column=4)

    def create_widgets(self) -> None:
        self.__frame_menu_mode = CTkFrame(self.root_window)
        self.__frame_menu_mode.grid(row=0, column=0)

        label = CTkLabel(self.__frame_menu_mode,text="---Change Game Mode---")
        label.grid(row=0, column=1)

        self.btn_single = self.__create_botton(self.__frame_menu_mode, 'single',300)
        self.btn_single.grid(row=1, column=1)

        self.btn_multi = self.__create_botton(self.__frame_menu_mode, 'multi',300)
        self.btn_multi.grid(row=2, column=1)

        self.btn_back = self.__create_botton(self.__frame_menu_mode, 'back', 300)
        self.btn_back.grid(row=3, column=1)

    def add_handler_easy(self, handler) -> None:
        self.btn_easy.configure(command=handler)

    def add_handler_medium(self,handler) -> None:
        self.btn_medium.configure(command=handler)

    def add_handler_hard(self,handler) -> None:
        self.btn_hard.configure(command=handler)

    def add_handler_single(self,handler) -> None:
        self.btn_single.configure(command=handler)

    def add_handler_multi(self,handler) -> None:
        self.btn_multi.configure(command=handler)

    def add_handler_back(self,handler) -> None:
        self.btn_back.configure(command=handler)