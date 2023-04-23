import unittest
from service.grid import GameGrid


class TestGameGrid(unittest.TestCase):
    def setUp(self):
        self.game = GameGrid()

    def test_get_pos_works(self):
        self.assertEqual(self.game.get_pos(), (0, 0))

    def test_cant_move_if_game_complete(self):
        self.game._complete = True
        self.game.move_pos('right')
        self.assertEqual(self.game._pos, [0, 0])

    def test_move_pos_doesnt_change(self):
        self.game.move_pos('left')
        self.assertEqual(self.game._pos, [0, 0])
        self.game.move_pos('up')
        self.assertEqual(self.game._pos, [0, 0])

    def test_move_pos_down_right_doesnt_change(self):
        self.game._pos = [8, 8]
        self.game.move_pos('right')
        self.assertEqual(self.game._pos, [8, 8])
        self.game.move_pos('down')
        self.assertEqual(self.game._pos, [8, 8])

    def test_move_pos_works(self):
        self.game._pos = [2, 3]
        self.game.move_pos('up')
        self.assertEqual(self.game._pos, [2, 2])
        self.game.move_pos('left')
        self.assertEqual(self.game._pos, [1, 2])
        self.game.move_pos('right')
        self.assertEqual(self.game._pos, [2, 2])
        self.game.move_pos('down')
        self.assertEqual(self.game._pos, [2, 3])

    def test_check_if_complete_returns_true(self):
        self.game._grid._grid = [[1, 2, 3, 6, 7, 8, 9, 4, 5],
                                 [5, 8, 4, 2, 3, 9, 7, 6, 1],
                                 [9, 6, 7, 1, 4, 5, 3, 2, 8],
                                 [3, 7, 2, 4, 6, 1, 5, 8, 9],
                                 [6, 9, 1, 5, 8, 3, 2, 7, 4],
                                 [4, 5, 8, 7, 9, 2, 6, 1, 3],
                                 [8, 3, 6, 9, 2, 4, 1, 5, 7],
                                 [2, 1, 9, 8, 5, 7, 4, 3, 6],
                                 [7, 4, 5, 3, 1, 6, 8, 9, 2]]
        self.assertTrue(self.game.check_if_complete())

    def test_check_if_complete_returns_false(self):
        self.game._grid._grid = [[0, 2, 3, 6, 7, 8, 9, 4, 5],
                                 [5, 8, 4, 2, 3, 9, 7, 6, 1],
                                 [9, 6, 7, 1, 4, 5, 3, 2, 8],
                                 [3, 7, 2, 4, 6, 1, 5, 8, 9],
                                 [6, 9, 1, 5, 8, 3, 2, 7, 4],
                                 [4, 5, 8, 7, 9, 2, 6, 1, 3],
                                 [8, 3, 6, 9, 2, 4, 1, 5, 7],
                                 [2, 1, 9, 8, 5, 7, 4, 3, 6],
                                 [7, 4, 5, 3, 1, 6, 8, 9, 2]]
        self.assertFalse(self.game.check_if_complete())

    def test_insert_number_if_complete(self):
        self.game._grid._grid = [[1, 2, 3, 6, 7, 8, 9, 4, 5],
                                 [5, 8, 4, 2, 3, 9, 7, 6, 1],
                                 [9, 6, 7, 1, 4, 5, 3, 2, 8],
                                 [3, 7, 2, 4, 6, 1, 5, 8, 9],
                                 [6, 9, 1, 5, 8, 3, 2, 7, 4],
                                 [4, 5, 8, 7, 9, 2, 6, 1, 3],
                                 [8, 3, 6, 9, 2, 4, 1, 5, 7],
                                 [2, 1, 9, 8, 5, 7, 4, 3, 6],
                                 [7, 4, 5, 3, 1, 6, 8, 9, 2]]
        
        self.game._grid._start =  [[0, 2, 3, 6, 7, 8, 9, 4, 5],
                                 [5, 8, 4, 2, 3, 9, 7, 6, 1],
                                 [9, 6, 7, 1, 4, 5, 3, 2, 8],
                                 [3, 7, 2, 4, 6, 1, 5, 8, 9],
                                 [6, 9, 1, 5, 8, 3, 2, 7, 4],
                                 [4, 5, 8, 7, 9, 2, 6, 1, 3],
                                 [8, 3, 6, 9, 2, 4, 1, 5, 7],
                                 [2, 1, 9, 8, 5, 7, 4, 3, 6],
                                 [7, 4, 5, 3, 1, 6, 8, 9, 2]]
        self.game._complete = True
        self.game.insert_number(4)
        self.assertEqual(self.game._grid._grid[0][0], 1)

    def test_insert_valid_number(self):
        self.game._grid._grid = [[0, 2, 3, 6, 7, 8, 9, 4, 5],
                                 [5, 8, 4, 2, 3, 9, 7, 6, 1],
                                 [9, 6, 7, 1, 4, 5, 3, 2, 8],
                                 [3, 7, 2, 4, 6, 1, 5, 8, 9],
                                 [6, 9, 1, 5, 8, 3, 2, 7, 4],
                                 [4, 5, 8, 7, 9, 2, 6, 1, 3],
                                 [8, 3, 6, 9, 2, 4, 1, 5, 7],
                                 [2, 1, 9, 8, 5, 7, 4, 3, 6],
                                 [7, 4, 5, 3, 1, 6, 8, 9, 2]]
        
        self.game._grid._start =  [[0, 2, 3, 6, 7, 8, 9, 4, 5],
                                 [5, 8, 4, 2, 3, 9, 7, 6, 1],
                                 [9, 6, 7, 1, 4, 5, 3, 2, 8],
                                 [3, 7, 2, 4, 6, 1, 5, 8, 9],
                                 [6, 9, 1, 5, 8, 3, 2, 7, 4],
                                 [4, 5, 8, 7, 9, 2, 6, 1, 3],
                                 [8, 3, 6, 9, 2, 4, 1, 5, 7],
                                 [2, 1, 9, 8, 5, 7, 4, 3, 6],
                                 [7, 4, 5, 3, 1, 6, 8, 9, 2]]
        self.game.insert_number(1)
        self.assertEqual(self.game._grid._grid[0][0], 1)

    def test_insert_valid_number_filled_number_increases(self):
        self.game._grid._grid = [[0, 2, 3, 6, 7, 8, 9, 4, 5],
                                 [5, 8, 4, 2, 0, 9, 7, 6, 1],
                                 [9, 6, 7, 1, 4, 5, 3, 2, 8],
                                 [3, 7, 2, 4, 6, 1, 5, 8, 9],
                                 [6, 9, 1, 5, 8, 3, 2, 7, 4],
                                 [4, 5, 8, 7, 9, 2, 6, 1, 3],
                                 [8, 3, 6, 9, 2, 4, 1, 5, 7],
                                 [2, 1, 9, 8, 5, 7, 4, 3, 6],
                                 [7, 4, 5, 3, 1, 6, 8, 9, 2]]
        
        self.game._grid._start = [[0, 2, 3, 6, 7, 8, 9, 4, 5],
                                 [5, 8, 4, 2, 0, 9, 7, 6, 1],
                                 [9, 6, 7, 1, 4, 5, 3, 2, 8],
                                 [3, 7, 2, 4, 6, 1, 5, 8, 9],
                                 [6, 9, 1, 5, 8, 3, 2, 7, 4],
                                 [4, 5, 8, 7, 9, 2, 6, 1, 3],
                                 [8, 3, 6, 9, 2, 4, 1, 5, 7],
                                 [2, 1, 9, 8, 5, 7, 4, 3, 6],
                                 [7, 4, 5, 3, 1, 6, 8, 9, 2]]
        self.game._filled = 79
        self.game.insert_number(1)
        self.assertEqual(self.game._filled, 80)

    def test_insert_0_and_filled_number_decreases(self):
        self.game._grid._grid = [[4, 2, 3, 6, 7, 8, 9, 0, 5],
                                 [5, 8, 4, 2, 3, 9, 7, 6, 1],
                                 [9, 6, 7, 1, 4, 5, 3, 2, 8],
                                 [3, 7, 2, 4, 6, 1, 5, 8, 9],
                                 [6, 9, 1, 5, 8, 3, 2, 7, 4],
                                 [4, 5, 8, 7, 9, 2, 6, 1, 3],
                                 [8, 3, 6, 9, 2, 4, 1, 5, 7],
                                 [2, 1, 9, 8, 5, 7, 4, 3, 6],
                                 [7, 4, 5, 3, 1, 6, 8, 9, 2]]
        
        self.game._grid._start = [[0, 2, 3, 6, 7, 8, 9, 0, 5],
                                 [5, 8, 4, 2, 0, 9, 7, 6, 1],
                                 [9, 6, 7, 1, 4, 5, 3, 2, 8],
                                 [3, 7, 2, 4, 6, 1, 5, 8, 9],
                                 [6, 9, 1, 5, 8, 3, 2, 7, 4],
                                 [4, 5, 8, 7, 9, 2, 6, 1, 3],
                                 [8, 3, 6, 9, 2, 4, 1, 5, 7],
                                 [2, 1, 9, 8, 5, 7, 4, 3, 6],
                                 [7, 4, 5, 3, 1, 6, 8, 9, 2]]
        self.game._filled = 80
        self.game.insert_number(0)
        self.assertEqual(self.game._filled, 79)

    def test_insert_number_to_complete(self):
        self.game._grid._grid = [[0, 2, 3, 6, 7, 8, 9, 4, 5],
                                 [5, 8, 4, 2, 3, 9, 7, 6, 1],
                                 [9, 6, 7, 1, 4, 5, 3, 2, 8],
                                 [3, 7, 2, 4, 6, 1, 5, 8, 9],
                                 [6, 9, 1, 5, 8, 3, 2, 7, 4],
                                 [4, 5, 8, 7, 9, 2, 6, 1, 3],
                                 [8, 3, 6, 9, 2, 4, 1, 5, 7],
                                 [2, 1, 9, 8, 5, 7, 4, 3, 6],
                                 [7, 4, 5, 3, 1, 6, 8, 9, 2]]
        
        self.game._grid._start =  [[0, 2, 3, 6, 7, 8, 9, 4, 5],
                                 [5, 8, 4, 2, 3, 9, 7, 6, 1],
                                 [9, 6, 7, 1, 4, 5, 3, 2, 8],
                                 [3, 7, 2, 4, 6, 1, 5, 8, 9],
                                 [6, 9, 1, 5, 8, 3, 2, 7, 4],
                                 [4, 5, 8, 7, 9, 2, 6, 1, 3],
                                 [8, 3, 6, 9, 2, 4, 1, 5, 7],
                                 [2, 1, 9, 8, 5, 7, 4, 3, 6],
                                 [7, 4, 5, 3, 1, 6, 8, 9, 2]]
        self.game._filled = 80
        self.game.insert_number(1)
        self.assertTrue(self.game._complete)
