from tkinter import messagebox
import logging
logging.basicConfig(level=logging.INFO,
                    filename="steps_history.log",
                    filemode="a",
                    format="%(asctime)s %(message)s")

from src.Statistics import StatsOperation



class Judge:


    def __init__(self):
        self.__steps = 0


    def set_steps_null(self) -> None:
        self.__steps = 0

    def __game_is_over(self, board, player1, player2):

        board_cells = board.get_cells()

        if self.__winner_is(board_cells, player1, player2):
            board.clear()
            self.set_steps_null()
            return True
        return False

    def __change_player(self, board) -> None:
        return board.change_player()

    def __player_do_step(self, player1, player2, cell, board) -> bool:

        if cell.is_empty():
            if self.__steps % 2 == 0:
                player2.do_move(cell)
                logging.info(f'#{self.__steps+1} User: {player2.get_name()} | Step: {cell.get_row_column()} | Side: {player2.get_side()}')
            else:
                player1.do_move(cell)
                logging.info(f'#{self.__steps+1} User: {player1.get_name()} | Step: {cell.get_row_column()} | Side: {player1.get_side()}')

            self.__steps += 1
            self.__change_player(board)
            return True

    def __bot_do_step(self, bot, board, difficulty: str) -> None:

        cell = bot.do_move(difficulty, board)
        logging.info(f'#{self.__steps+1} User: {bot.get_name()}     | Step: {cell.get_row_column()} | Side: {bot.get_side()}')

        self.__steps += 1
        self.__change_player(board)

    def __winner_is(self, board_cells: list[list], player1, player2):
        return Rules.winner_is(board_cells, player1, player2)

    def check_winner_str(self, board, side) -> bool:
        return Rules.check_winner_str(board, side)

    def game_with_player(self, player1, player2, cell, board) -> None:

        self.__player_do_step(player1,player2, cell, board)
        self.__game_is_over(board, player1, player2)

    def game_with_pc(self, bot, player2, cell, board, difficulty) -> None:

        if self.__player_do_step(bot, player2, cell, board) and not self.__game_is_over(board, bot, player2) :

            board.do_sleep(lambda : (self.__bot_do_step(bot, board, difficulty),
                                           self.__game_is_over(board, bot, player2)) )



class Rules:

        @staticmethod
        def check_winner_str(board, side) -> bool:
            return ((board[0][0] == side and board[0][1] == side and board[0][2] == side) or
                    (board[1][0] == side and board[1][1] == side and board[1][2] == side) or
                    (board[2][0] == side and board[2][1] == side and board[2][2] == side) or
                    (board[0][0] == side and board[1][0] == side and board[2][0] == side) or
                    (board[0][1] == side and board[1][1] == side and board[2][1] == side) or
                    (board[0][2] == side and board[1][2] == side and board[2][2] == side) or
                    (board[0][0] == side and board[1][1] == side and board[2][2] == side) or
                    (board[0][2] == side and board[1][1] == side and board[2][0] == side))

        @staticmethod
        def check_winner_cell(board, side) -> bool:
            return ((board[0][0].get_value() == side and board[0][1].get_value() == side and board[0][
                2].get_value() == side) or
                    (board[1][0].get_value() == side and board[1][1].get_value() == side and board[1][
                        2].get_value() == side) or
                    (board[2][0].get_value() == side and board[2][1].get_value() == side and board[2][
                        2].get_value() == side) or
                    (board[0][0].get_value() == side and board[1][0].get_value() == side and board[2][
                        0].get_value() == side) or
                    (board[0][1].get_value() == side and board[1][1].get_value() == side and board[2][
                        1].get_value() == side) or
                    (board[0][2].get_value() == side and board[1][2].get_value() == side and board[2][
                        2].get_value() == side) or
                    (board[0][0].get_value() == side and board[1][1].get_value() == side and board[2][
                        2].get_value() == side) or
                    (board[0][2].get_value() == side and board[1][1].get_value() == side and board[2][
                        0].get_value() == side))

        @staticmethod
        def gameboard_is_full(board) -> bool:

            for row in board:
                for elem in row:
                    if elem.get_value() == '':
                        return False
            return True

        @staticmethod
        def winner_is(board_cells, player1, player2) -> bool:

            if Rules.check_winner_cell(board_cells, player2.get_side()):
                messagebox.showinfo("Winner", f"X won the match")
                StatsOperation().save(f"{player2.get_name()} - Won - {player1.get_name()}")
                logging.info("X won the match")
                return True

            if Rules.check_winner_cell(board_cells, player1.get_side()):
                messagebox.showinfo("Winner", f"O won the match")
                StatsOperation().save(f"{player1.get_name()} - Won - {player2.get_name()}")
                logging.info("O won the match")
                return True

            if Rules.gameboard_is_full(board_cells):
                messagebox.showinfo("Tie Game", "Tie Game")
                StatsOperation().save(f"{player2.get_name()} - Tie Game - {player1.get_name()}")
                logging.info("Tie Game")
                return True