from __future__ import annotations
import customtkinter
from customtkinter import *
import json

import config



class Statistics:


    def __init__(self, root, menu_mode):
        self.__root = root
        self.__menu_mode = menu_mode
        self.__viewer = StatisticsViewer(self.__root)


    def __registration_events_bottons_menu(self):
        self.__viewer.add_handler_back(self.__handler_on_click_back)

    def __handler_on_click_back(self):
        self.__viewer.clear_menu_stats()
        self.__menu_mode.draw()

    def draw(self):
        self.__viewer.create_widgets()
        self.__registration_events_bottons_menu()



class StatisticsViewer:


    def __init__(self, root):
        self.root_window = root


    def __create_botton(self, frame, text):
        return CTkButton(frame, text= text, height=50)

    def __create_output_data(self):
        self.__data = StatsOperation().read_json()
        for item, value in self.__data.items():
            self.textbox.insert('end',f'#{item}  {value}\n' )

    def clear_menu_stats(self):
        self.__menu_stats.destroy()

    def create_widgets(self):
        self.__menu_stats = CTkFrame(self.root_window)
        self.__menu_stats.grid(row=0, column=0)

        label = CTkLabel(self.__menu_stats, text="---Statistics---")
        label.grid(row=0, column=0, sticky="ew")

        all_game = CTkLabel(self.__menu_stats, text = f"All game: {StatsOperation().get_count_game() - 1}")
        all_game.grid(row=0, column=1, sticky="ew")

        self.textbox = customtkinter.CTkTextbox(master=self.__menu_stats, width=350)
        self.textbox.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="nsew", columnspan=2)
        self.__create_output_data()

        self.btn_back = self.__create_botton(self.__menu_stats, 'back')
        self.btn_back.grid(row=2, column=0, columnspan=2)

    def add_handler_back(self,handler):
        self.btn_back.configure(command=handler)



class StatsOperation:


    def __init__(self):
        self.__path_file = config.STATS_FILE
        self.__new_data = {}
        self.__old_data = self.read_json()
        self.__game_counter = self.__take_game_counter() + 1

    def stats_is_empty(self):
        return self.read_json() == {} and self.read_log() == ''

    def get_count_game(self):
        return self.__game_counter

    def __take_game_counter(self):
        return len(self.__old_data.keys())

    def read_json(self):
        with open(self.__path_file, 'r') as jsonfile:
            data = json.load(jsonfile)
            return data

    def read_log(self):
        with open('steps_history.log', 'r') as log:
            data = log.read()
            return data

    def save(self, value):
        self.__new_data[self.__game_counter] = value
        self.__old_data.update(self.__new_data)
        self.__game_counter += 1
        with open(self.__path_file, 'w') as jsonfile:
            json.dump(self.__old_data, jsonfile)

    def clear(self):
        with open(self.__path_file, 'w') as jsonfile:
            json.dump({}, jsonfile)
        open('steps_history.log', 'w').close()