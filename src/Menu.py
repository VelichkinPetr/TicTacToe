from __future__ import annotations
import customtkinter
from customtkinter import *
from PIL import Image

import  config
from src.MenuMode import MenuMode
from src.Statistics import Statistics, StatsOperation



class Menu:

    def __init__(self, root: CTk, game):
        self.__root = root
        self.__viewer = MenuViewer(self.__root)
        self.__menu_mode = MenuMode(self.__root, self, game)
        self.__menu_stats = Statistics(self.__root, self)


    def __registration_events_bottons_menu(self) -> None:
        self.__viewer.add_handler_start(self.__handler_on_click_start)
        self.__viewer.add_handler_statistics(self.__handler_on_click_statistics)
        self.__viewer.add_handler_exit(self.__handler_on_click_exit)
        self.__viewer.add_handler_cache_clean(self.__handler_on_click_cache_clean)

    def __handler_on_click_start(self) -> None:
        self.__viewer.clear()
        self.__menu_mode.draw()

    def __handler_on_click_exit(self) -> None:
        self.__root.destroy()

    def __handler_on_click_statistics(self) -> None:
        self.__viewer.clear()
        self.__menu_stats.draw()

    def __handler_on_click_cache_clean(self) -> None:
        dialog = customtkinter.CTkInputDialog(text="Enter 'Clean' to clear the cache:", title="Cache Clean")
        if dialog.get_input() == 'Clean':
            StatsOperation().clear()
            self.__viewer.btn_cache_clean.configure(image= self.__viewer.image_recycle_empty)

    def draw(self) -> None:
        self.__viewer.create_widgets()
        self.__registration_events_bottons_menu()



class MenuViewer:

    def __init__(self, root: CTk):
        self.root_window = root
        self.switch_var = customtkinter.StringVar(value="off")
        self.switch_text = 'light'
        self.image_recycle_full = CTkImage(light_image=Image.open(config.IMAGE_RECYCLE_FULL), size=(40, 40))
        self.image_recycle_empty = CTkImage(light_image=Image.open(config.IMAGE_RECYCLE_EMPTY), size=(40, 40))

    def __create_botton(self, frame, text: str, width: int) -> CTkButton:
        return CTkButton(frame, text=text,height=50, width=width)

    def __switch_event(self) -> None:
        if self.switch_var.get() == ('on'):
            self.switch_text = 'dark'
        else:
            self.switch_text = 'light'
        self.switch.configure(text=self.switch_text)
        customtkinter.set_appearance_mode(self.switch_text)

    def clear(self) -> None: self.__frame_menu.destroy()

    def create_widgets(self) -> None:

        self.__frame_menu = CTkFrame(master=self.root_window)
        self.__frame_menu.grid(row=0, column=0,sticky="nsew")

        label = CTkLabel(self.__frame_menu,text="---Welcome to tic-tac-toe---")

        label.grid(row=0, column=0,sticky="ew", columnspan=2)

        self.btn_start = self.__create_botton(self.__frame_menu, 'start', 300)
        self.btn_start.grid(row=1, column=0,sticky="ew", columnspan=2)

        self.btn_statistics = self.__create_botton(self.__frame_menu,'statistics', 300)
        self.btn_statistics.grid(row=3, column=0,sticky="ew", columnspan=2)

        self.btn_exit = self.__create_botton(self.__frame_menu, 'exit',  300)
        self.btn_exit.grid(row=5, column=0,sticky="ew", columnspan=2)

        self.switch = customtkinter.CTkSwitch(self.__frame_menu, text=self.switch_text, command=self.__switch_event,
                                         variable=self.switch_var, onvalue="on", offvalue="off")
        self.switch.grid(row=6, column=0, padx=10, pady=10, sticky="ew")

        if StatsOperation().stats_is_empty():
            self.btn_cache_clean = CTkButton(self.__frame_menu, image=self.image_recycle_empty, text="", width=50, height=50, fg_color = ("#D3CFFC", "#5D3A4A"))
        else:
            self.btn_cache_clean = CTkButton(self.__frame_menu, image=self.image_recycle_full, text="", width=50, height=50, fg_color = ("#D3CFFC", "#5D3A4A"))

        self.btn_cache_clean.grid(row=6, column=1,sticky="ew")

    def add_handler_start(self, handler) -> None:
        self.btn_start.configure(command=handler)

    def add_handler_exit(self, handler) -> None:
        self.btn_exit.configure(command=handler)

    def add_handler_statistics(self, handler) -> None:
        self.btn_statistics.configure(command=handler)

    def add_handler_cache_clean(self, handler) -> None:
        self.btn_cache_clean.configure(command=handler)