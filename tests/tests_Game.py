import unittest
from customtkinter import *
from src.Gameboard import GameBoard
from src.Judge import Judge, Rules
from src.User import User

# Все возможные варианты Побед
#   -Проверили модули GameBoard, Player, Judge

class GameTest(unittest.TestCase):
    def setUp(self):
        self.root = CTk()
        self.j = Judge()
        self.pl1 = User.create(1, 'Gamer 1', 'X')
        self.pl2 = User.create(1, 'Gamer 2', 'O')
        self.bot = User.create(2, 'Bot', 'O')
        self.b = GameBoard(self.root, self.j, [self.bot, self.pl2, self.pl1])
        self.cells = self.b.get_cells()
        self.b.draw(2,'')

# Board is not filled
    #all row win O
    def test_row_0_win_O(self):
        '''
        pl1 = X
        pl2 = O

        [o,o,o]
        [ , , ]
        [x, ,x]
        :return: Win O
        '''
        self.assertFalse(Rules.winner_is(self.b.get_cells(),self.pl1,self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(),self.pl1,self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(),self.pl1,self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(),self.pl1,self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))

        self.assertTrue(self.pl2.do_move(self.cells[0][1]))
        self.assertTrue(Rules.check_winner_cell(self.cells, self.pl2.get_side()))

    def test_row_1_win_O(self):
        '''
        pl1 = X
        pl2 = O

        [ , , ]
        [o,o,o]
        [x, ,x]
        :return: Win O
        '''
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[1][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[1][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))

        self.assertTrue(self.pl2.do_move(self.cells[1][1]))
        self.assertTrue(Rules.check_winner_cell(self.cells, self.pl2.get_side()))

    def test_row_2_win_O(self):
        '''
        pl1 = X
        pl2 = O

        [ , , ]
        [x, ,x]
        [o,o,o]

        :return: Win O
        '''
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[1][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[1][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))

        self.assertTrue(self.pl2.do_move(self.cells[2][1]))
        self.assertTrue(Rules.check_winner_cell(self.cells, self.pl2.get_side()))

    # all column win O
    def test_column_0_win_O(self):
        '''
        pl1 = X
        pl2 = O

        [o, ,x]
        [o, , ]
        [o, ,x]
        :return: Win O
        '''
        self.assertFalse(Rules.winner_is(self.b.get_cells(),self.pl1,self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(),self.pl1,self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(),self.pl1,self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(),self.pl1,self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))

        self.assertTrue(self.pl2.do_move(self.cells[1][0]))
        self.assertTrue(Rules.check_winner_cell(self.cells, self.pl2.get_side()))

    def test_column_1_win_O(self):
        '''
        pl1 = X
        pl2 = O

        [ ,o,x]
        [ ,o, ]
        [ ,o,x]
        :return: Win O
        '''
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))

        self.assertTrue(self.pl2.do_move(self.cells[1][1]))
        self.assertTrue(Rules.check_winner_cell(self.cells, self.pl2.get_side()))

    def test_column_2_win_O(self):
        '''
        pl1 = X
        pl2 = O

        [ ,x,o]
        [ , ,o]
        [ ,x,o]
        :return: Win O
        '''
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))

        self.assertTrue(self.pl2.do_move(self.cells[1][2]))
        self.assertTrue(Rules.check_winner_cell(self.cells, self.pl2.get_side()))

    # all diag win O
    def test_first_diagonal_win_O(self):
        '''
        pl1 = X
        pl2 = O

        [o, , ]
        [x,o, ]
        [x, ,o]

        :return: Win O
        '''
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[1][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[1][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))

        self.assertTrue(self.pl2.do_move(self.cells[2][2]))
        self.assertTrue(Rules.check_winner_cell(self.cells, self.pl2.get_side()))

    def test_second_diagonal_win_O(self):
        '''
        pl1 = X
        pl2 = O

        [ , ,o]
        [x,o, ]
        [o,x, ]

        :return: Win X
        '''
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[1][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[1][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))

        self.assertTrue(self.pl2.do_move(self.cells[2][0]))
        self.assertTrue(Rules.check_winner_cell(self.cells, self.pl2.get_side()))

    # all row win X
    def test_row_0_win_X(self):
        '''
        pl1 = X
        pl2 = O

        [x,x,x]
        [ , , ]
        [o, ,o]
        :return: Win X
        '''
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))

        self.assertTrue(self.pl1.do_move(self.cells[0][1]))
        self.assertTrue(Rules.check_winner_cell(self.cells, self.pl1.get_side()))

    def test_row_1_win_X(self):
        '''
        pl1 = X
        pl2 = O

        [ , , ]
        [x,x,x]
        [o, ,o]
        :return: Win X
        '''
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[1][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[1][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))

        self.assertTrue(self.pl1.do_move(self.cells[1][1]))
        self.assertTrue(Rules.check_winner_cell(self.cells, self.pl1.get_side()))

    def test_row_2_win_X(self):
        '''
        pl1 = X
        pl2 = O

        [ , , ]
        [o, ,o]
        [x,x,x]

        :return: Win X
        '''
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[1][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[1][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))

        self.assertTrue(self.pl1.do_move(self.cells[2][1]))
        self.assertTrue(Rules.check_winner_cell(self.cells, self.pl1.get_side()))

    # all column win X
    def test_column_0_win_X(self):
        '''
        pl1 = X
        pl2 = O

        [x, ,o]
        [x, , ]
        [x, ,o]
        :return: Win X
        '''
        self.assertFalse(Rules.winner_is(self.b.get_cells(),self.pl1,self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(),self.pl1,self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(),self.pl1,self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(),self.pl1,self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))

        self.assertTrue(self.pl1.do_move(self.cells[1][0]))
        self.assertTrue(Rules.check_winner_cell(self.cells, self.pl1.get_side()))

    def test_column_1_win_X(self):
        '''
        pl1 = X
        pl2 = O

        [ ,x,o]
        [ ,x, ]
        [ ,x,o]
        :return: Win X
        '''
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))

        self.assertTrue(self.pl1.do_move(self.cells[1][1]))
        self.assertTrue(Rules.check_winner_cell(self.cells, self.pl1.get_side()))

    def test_column_2_win_X(self):
        '''
        pl1 = X
        pl2 = O

        [ ,o,x]
        [ , ,x]
        [ ,o,x]
        :return: Win X
        '''
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))

        self.assertTrue(self.pl1.do_move(self.cells[1][2]))
        self.assertTrue(Rules.check_winner_cell(self.cells, self.pl1.get_side()))

    # all diag win X
    def test_first_diagonal_win_X(self):
        '''
        pl1 = X
        pl2 = O

        [x, , ]
        [o,x, ]
        [o, ,x]

        :return: Win X
        '''
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[1][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[1][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))

        self.assertTrue(self.pl1.do_move(self.cells[2][2]))
        self.assertTrue(Rules.check_winner_cell(self.cells, self.pl1.get_side()))

    def test_second_diagonal_win_X(self):
        '''
        pl1 = X
        pl2 = O

        [ , ,x]
        [o,x, ]
        [x,o, ]

        :return: Win X
        '''
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[1][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[1][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))

        self.assertTrue(self.pl1.do_move(self.cells[2][0]))
        self.assertTrue(Rules.check_winner_cell(self.cells, self.pl1.get_side()))



# Board is filled
    # all row win O
    def test_row_0_win_O_filled(self):
        '''
        pl1 = X
        pl2 = O

        [o,o,o]
        [x,x,o]
        [x,o,x]
        :return: Win O
        '''
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[1][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[1][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[1][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))

        self.assertTrue(self.pl2.do_move(self.cells[0][1]))
        self.assertTrue(Rules.check_winner_cell(self.cells, self.pl2.get_side()))

    def test_row_1_win_O_filled(self):
        '''
        pl1 = X
        pl2 = O

        [x,x,o]
        [o,o,o]
        [x,o,x]
        :return: Win O
        '''
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[1][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[1][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))

        self.assertTrue(self.pl2.do_move(self.cells[1][1]))
        self.assertTrue(Rules.check_winner_cell(self.cells, self.pl2.get_side()))

    def test_row_2_win_O_filled(self):
        '''
        pl1 = X
        pl2 = O

        [x,o,x]
        [o,x,x]
        [o,o,o]

        :return: Win O
        '''
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[1][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[1][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[1][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))

        self.assertTrue(self.pl2.do_move(self.cells[2][1]))
        self.assertTrue(Rules.check_winner_cell(self.cells, self.pl2.get_side()))

    # all column win O
    def test_column_0_win_O_filled(self):
        '''
        pl1 = X
        pl2 = O

        [o,o,x]
        [o,x,o]
        [o,x,x]
        :return: Win O
        '''
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[1][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[1][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))

        self.assertTrue(self.pl2.do_move(self.cells[1][0]))
        self.assertTrue(Rules.check_winner_cell(self.cells, self.pl2.get_side()))

    def test_column_1_win_O_filled(self):
        '''
        pl1 = X
        pl2 = O

        [x,o,x]
        [x,o,o]
        [o,o,x]
        :return: Win O
        '''
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[1][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[1][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))

        self.assertTrue(self.pl2.do_move(self.cells[1][1]))
        self.assertTrue(Rules.check_winner_cell(self.cells, self.pl2.get_side()))

    def test_column_2_win_O_filled(self):
        '''
        pl1 = X
        pl2 = O

        [x,x,o]
        [o,x,o]
        [x,o,o]
        :return: Win O
        '''
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[1][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[1][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))

        self.assertTrue(self.pl2.do_move(self.cells[1][2]))
        self.assertTrue(Rules.check_winner_cell(self.cells, self.pl2.get_side()))

    # all diag win O
    def test_first_diagonal_win_O_filled(self):
        '''
        pl1 = X
        pl2 = O

        [o,x,o]
        [x,o,x]
        [x,x,o]

        :return: Win O
        '''
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[1][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[1][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[1][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))

        self.assertTrue(self.pl2.do_move(self.cells[2][2]))
        self.assertTrue(Rules.check_winner_cell(self.cells, self.pl2.get_side()))

    def test_second_diagonal_win_O_filled(self):
        '''
        pl1 = X
        pl2 = O

        [x,o,o]
        [x,o,x]
        [o,x,o]

        :return: Win O
        '''
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[1][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[1][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[1][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))

        self.assertTrue(self.pl2.do_move(self.cells[2][0]))
        self.assertTrue(Rules.check_winner_cell(self.cells, self.pl2.get_side()))

    # all row win X
    def test_row_0_win_X_filled(self):
        '''
        pl1 = X
        pl2 = O

        [X,X,X]
        [O,O,X]
        [O,X,O]
        :return: Win X
        '''
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[1][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[1][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[1][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))

        self.assertTrue(self.pl1.do_move(self.cells[0][1]))
        self.assertTrue(Rules.check_winner_cell(self.cells, self.pl1.get_side()))

    def test_row_1_win_X_filled(self):
        '''
        pl1 = X
        pl2 = O

        [O,O,X]
        [X,X,X]
        [O,X,O]
        :return: Win X
        '''
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[1][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[1][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))

        self.assertTrue(self.pl1.do_move(self.cells[1][1]))
        self.assertTrue(Rules.check_winner_cell(self.cells, self.pl1.get_side()))

    def test_row_2_win_X_filled(self):
        '''
        pl1 = X
        pl2 = O

        [O,X,O]
        [X,O,O]
        [X,X,X]

        :return: Win X
        '''
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[1][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[1][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[1][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))

        self.assertTrue(self.pl1.do_move(self.cells[2][1]))
        self.assertTrue(Rules.check_winner_cell(self.cells, self.pl1.get_side()))

    # all column win X
    def test_column_0_win_X_filled(self):
        '''
        pl1 = X
        pl2 = O

        [X,X,O]
        [X,O,X]
        [X,O,O]
        :return: Win X
        '''
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[1][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[1][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))

        self.assertTrue(self.pl1.do_move(self.cells[1][0]))
        self.assertTrue(Rules.check_winner_cell(self.cells, self.pl1.get_side()))

    def test_column_1_win_X_filled(self):
        '''
        pl1 = X
        pl2 = O

        [O,X,O]
        [O,X,X]
        [X,X,O]
        :return: Win X
        '''
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[1][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[1][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))

        self.assertTrue(self.pl1.do_move(self.cells[1][1]))
        self.assertTrue(Rules.check_winner_cell(self.cells, self.pl1.get_side()))

    def test_column_2_win_X_filled(self):
        '''
        pl1 = X
        pl2 = O

        [O,O,X]
        [X,O,X]
        [O,X,X]
        :return: Win X
        '''
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[1][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[1][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))

        self.assertTrue(self.pl1.do_move(self.cells[1][2]))
        self.assertTrue(Rules.check_winner_cell(self.cells, self.pl1.get_side()))

    # all diag win X
    def test_first_diagonal_win_X_filled(self):
        '''
        pl1 = X
        pl2 = O

        [X,O,X]
        [O,X,O]
        [O,O,X]

        :return: Win X
        '''
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[1][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[1][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[1][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))

        self.assertTrue(self.pl1.do_move(self.cells[2][2]))
        self.assertTrue(Rules.check_winner_cell(self.cells, self.pl1.get_side()))

    def test_second_diagonal_win_X_filled(self):
        '''
        pl1 = X
        pl2 = O

        [O,X,X]
        [O,X,O]
        [X,O,X]

        :return: Win X
        '''
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[1][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[1][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[1][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))

        self.assertTrue(self.pl1.do_move(self.cells[2][0]))
        self.assertTrue(Rules.check_winner_cell(self.cells, self.pl1.get_side()))



    def test_tie(self):
        '''
        pl1 = X
        pl2 = O

        [o,x,o]
        [o,x,x]
        [x,o,x]

        :return: Tie
        '''
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[0][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[1][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[1][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[1][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[0][2]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl1.do_move(self.cells[2][0]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))
        self.assertTrue(self.pl2.do_move(self.cells[2][1]))
        self.assertFalse(Rules.winner_is(self.b.get_cells(), self.pl1, self.pl2))

        self.assertTrue(self.pl1.do_move(self.cells[2][2]))
        self.assertTrue(Rules.gameboard_is_full(self.cells))
