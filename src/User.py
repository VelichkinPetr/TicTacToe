import random
from copy import deepcopy

from src.Judge import Rules


class User:

    @staticmethod
    def create(access_level, name, side):
        if access_level == 1: user = Player(name, side)
        if access_level == 2: user = BotComputer(name, side)
        return user


class Player:


    def __init__(self, name, side):
        self._name = name
        self._side = side
        self._access_level = 1


    def get_side(self):
        return self._side

    def get_name(self):
        return self._name

    def do_move(self, cell):
        cell.change_value(self._side)
        return True


class BotComputer:


    def __init__(self, name, side):
        self._access_level = 2
        self._side = side
        self._name = name


    def get_side(self):
        return self._side

    def get_name(self):
        return self._name

    def __selecting_cell(self, mode, board):
        board_cells = board.get_cells()
        board_str = board.get_board_str()

        possible_move = []
        for i in range(len(board_str)):
            for j in range(len(board_str[i])):
                if board_str[i][j] == '':
                    possible_move.append([i, j])
        if possible_move == []:
            return

        if mode == 'easy':
            move = random.randint(0, len(possible_move) - 1)
            row, column = possible_move[move]

            return board_cells[row][column]

        if mode == 'medium':
            random_mode = random.choice(['easy', 'hard'])
            return self.__selecting_cell(random_mode, board)

        if mode == 'hard':

            for let in ['O', 'X']:
                for i in possible_move:
                    boardcopy = deepcopy(board_str)
                    boardcopy[i[0]][i[1]] = let
                    if Rules.check_winner_str(boardcopy, let):
                        return board_cells[i[0]][i[1]]

            corner = []
            for i in possible_move:
                if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
                    corner.append(i)
            if len(corner) > 0:
                move = random.randint(0, len(corner) - 1)
                row, column = corner[move]
                return board_cells[row][column]

            edge = []
            for i in possible_move:
                if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
                    edge.append(i)
            if len(edge) > 0:
                move = random.randint(0, len(edge) - 1)
                row, column = edge[move]
                return board_cells[row][column]

    def do_move(self, mode, board):
        cell = self.__selecting_cell(mode, board)
        cell.change_value(self._side)
        return cell