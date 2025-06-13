from customtkinter import *



class Cell:


    def __init__(self, frame: CTkFrame, row: int, column: int):
        self.__row = row
        self.__column = column
        self.__model = CellModel(row,column)
        self.__viewer = CellViewer(frame, self.__model.get_value())

    def clear(self) -> None:
        self.__model.clear()
        self.__viewer.clear()

    def create_cell(self) -> None:
        self.__viewer.create_widget(self.__row,self.__column)

    def add_handler_on_click(self, handler) -> None:
        self.__viewer.add_handler_btn(handler)

    def change_value(self, new_value) -> None:
        self.__model.change_value(new_value)
        self.__viewer.set_value(self.__model.get_value())
        self.__viewer.close_btn()

    def get_row_column(self) -> (int,int):
        return self.__model.get_row_column()

    def get_value(self) -> str:
        return self.__model.get_value()

    def is_empty(self) -> bool:
        return self.__model.is_empty()



class CellModel:


    def __init__(self, row: int, column: int):
        self.__value = ''
        self.__row = row
        self.__column = column

    def get_row_column(self) -> (int,int):
        return self.__row,self.__column

    def get_value(self) -> str:
        return self.__value

    def is_empty(self) -> bool:
        return self.__value == ''

    def clear(self) -> None:
        self.__value = ''

    def change_value(self, new_value) -> None:
        self.__value = new_value



class CellViewer:


    def __init__(self, frame: CTkFrame, value: str):
        self.__value = value
        self.__frame = frame

    def clear(self) -> None:
        self.set_value('')

    def set_value(self, new_value: str) -> None:
        self.__value = new_value
        self.btn.configure(text= self.__value, hover = True, state = NORMAL)

    def create_widget(self, row: int, column: int) -> None:
        self.btn = CTkButton(self.__frame, height=150, width=150, text=self.__value)
        self.btn.grid(row=row, column=column)

    def add_handler_btn(self, handler) -> None:
        self.btn.configure(command=handler)

    def close_btn(self) -> None:
        self.btn.configure(hover=False, state = DISABLED, text_color='black')