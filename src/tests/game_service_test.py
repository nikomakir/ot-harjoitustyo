import unittest
from service.game_service import GameService, NoSavedGame
from entities.sudoku import Sudoku


class FakeSudokuRepository:
    def __init__(self):
        self.grid = []
        self.start = []
        self.filled = 0

    def delete(self):
        self.grid.clear()
        self.start.clear()
        self.filled = 0

    def write(self, filled, grid, start):
        self.grid = grid
        self.start = start
        self.filled = filled

    def load(self):
        return self.grid, self.start, self.filled


class TestGameService(unittest.TestCase):
    def setUp(self):
        self.game = GameService(FakeSudokuRepository())

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
        self.game._grid = Sudoku(0, [[1, 2, 3, 6, 7, 8, 9, 4, 5],
                                 [5, 8, 4, 2, 3, 9, 7, 6, 1],
                                 [9, 6, 7, 1, 4, 5, 3, 2, 8],
                                 [3, 7, 2, 4, 6, 1, 5, 8, 9],
                                 [6, 9, 1, 5, 8, 3, 2, 7, 4],
                                 [4, 5, 8, 7, 9, 2, 6, 1, 3],
                                 [8, 3, 6, 9, 2, 4, 1, 5, 7],
                                 [2, 1, 9, 8, 5, 7, 4, 3, 6],
                                 [7, 4, 5, 3, 1, 6, 8, 9, 2]])
        self.assertTrue(self.game.check_if_complete())

    def test_check_if_complete_returns_false(self):
        self.game._grid = Sudoku(0, [[0, 2, 3, 6, 7, 8, 9, 4, 5],
                                 [5, 8, 4, 2, 3, 9, 7, 6, 1],
                                 [9, 6, 7, 1, 4, 5, 3, 2, 8],
                                 [3, 7, 2, 4, 6, 1, 5, 8, 9],
                                 [6, 9, 1, 5, 8, 3, 2, 7, 4],
                                 [4, 5, 8, 7, 9, 2, 6, 1, 3],
                                 [8, 3, 6, 9, 2, 4, 1, 5, 7],
                                 [2, 1, 9, 8, 5, 7, 4, 3, 6],
                                 [7, 4, 5, 3, 1, 6, 8, 9, 2]])
        self.assertFalse(self.game.check_if_complete())

    def test_insert_number_if_complete(self):
        self.game._grid = Sudoku(0, [[1, 2, 3, 6, 7, 8, 9, 4, 5],
                                 [5, 8, 4, 2, 3, 9, 7, 6, 1],
                                 [9, 6, 7, 1, 4, 5, 3, 2, 8],
                                 [3, 7, 2, 4, 6, 1, 5, 8, 9],
                                 [6, 9, 1, 5, 8, 3, 2, 7, 4],
                                 [4, 5, 8, 7, 9, 2, 6, 1, 3],
                                 [8, 3, 6, 9, 2, 4, 1, 5, 7],
                                 [2, 1, 9, 8, 5, 7, 4, 3, 6],
                                 [7, 4, 5, 3, 1, 6, 8, 9, 2]],
                                 [[0, 2, 3, 6, 7, 8, 9, 4, 5],
                                  [5, 8, 4, 2, 3, 9, 7, 6, 1],
                                  [9, 6, 7, 1, 4, 5, 3, 2, 8],
                                  [3, 7, 2, 4, 6, 1, 5, 8, 9],
                                  [6, 9, 1, 5, 8, 3, 2, 7, 4],
                                  [4, 5, 8, 7, 9, 2, 6, 1, 3],
                                  [8, 3, 6, 9, 2, 4, 1, 5, 7],
                                  [2, 1, 9, 8, 5, 7, 4, 3, 6],
                                  [7, 4, 5, 3, 1, 6, 8, 9, 2]])

        self.game._complete = True
        self.game.insert_number(4)
        self.assertEqual(self.game._grid.grid[0][0], 1)

    def test_insert_valid_number(self):
        self.game._grid = Sudoku(0, [[0, 2, 3, 6, 7, 8, 9, 4, 5],
                                 [5, 8, 4, 2, 3, 9, 7, 6, 1],
                                 [9, 6, 7, 1, 4, 5, 3, 2, 8],
                                 [3, 7, 2, 4, 6, 1, 5, 8, 9],
                                 [6, 9, 1, 5, 8, 3, 2, 7, 4],
                                 [4, 5, 8, 7, 9, 2, 6, 1, 3],
                                 [8, 3, 6, 9, 2, 4, 1, 5, 7],
                                 [2, 1, 9, 8, 5, 7, 4, 3, 6],
                                 [7, 4, 5, 3, 1, 6, 8, 9, 2]],
                                 [[0, 2, 3, 6, 7, 8, 9, 4, 5],
                                  [5, 8, 4, 2, 3, 9, 7, 6, 1],
                                  [9, 6, 7, 1, 4, 5, 3, 2, 8],
                                  [3, 7, 2, 4, 6, 1, 5, 8, 9],
                                  [6, 9, 1, 5, 8, 3, 2, 7, 4],
                                  [4, 5, 8, 7, 9, 2, 6, 1, 3],
                                  [8, 3, 6, 9, 2, 4, 1, 5, 7],
                                  [2, 1, 9, 8, 5, 7, 4, 3, 6],
                                  [7, 4, 5, 3, 1, 6, 8, 9, 2]])

        self.game._filled = 80
        self.game.insert_number(1)
        self.assertEqual(self.game._grid.grid[0][0], 1)

    def test_insert_valid_number_filled_number_increases(self):
        self.game._grid = Sudoku(0, [[0, 2, 3, 6, 7, 8, 9, 4, 5],
                                 [5, 8, 4, 2, 0, 9, 7, 6, 1],
                                 [9, 6, 7, 1, 4, 5, 3, 2, 8],
                                 [3, 7, 2, 4, 6, 1, 5, 8, 9],
                                 [6, 9, 1, 5, 8, 3, 2, 7, 4],
                                 [4, 5, 8, 7, 9, 2, 6, 1, 3],
                                 [8, 3, 6, 9, 2, 4, 1, 5, 7],
                                 [2, 1, 9, 8, 5, 7, 4, 3, 6],
                                 [7, 4, 5, 3, 1, 6, 8, 9, 2]],
                                 [[0, 2, 3, 6, 7, 8, 9, 4, 5],
                                  [5, 8, 4, 2, 0, 9, 7, 6, 1],
                                  [9, 6, 7, 1, 4, 5, 3, 2, 8],
                                  [3, 7, 2, 4, 6, 1, 5, 8, 9],
                                  [6, 9, 1, 5, 8, 3, 2, 7, 4],
                                  [4, 5, 8, 7, 9, 2, 6, 1, 3],
                                  [8, 3, 6, 9, 2, 4, 1, 5, 7],
                                  [2, 1, 9, 8, 5, 7, 4, 3, 6],
                                  [7, 4, 5, 3, 1, 6, 8, 9, 2]])

        self.game._filled = 79
        self.game.insert_number(1)
        self.assertEqual(self.game._filled, 80)

    def test_insert_0_and_filled_number_decreases(self):
        self.game._grid = Sudoku(0, [[4, 2, 3, 6, 7, 8, 9, 0, 5],
                                 [5, 8, 4, 2, 3, 9, 7, 6, 1],
                                 [9, 6, 7, 1, 4, 5, 3, 2, 8],
                                 [3, 7, 2, 4, 6, 1, 5, 8, 9],
                                 [6, 9, 1, 5, 8, 3, 2, 7, 4],
                                 [4, 5, 8, 7, 9, 2, 6, 1, 3],
                                 [8, 3, 6, 9, 2, 4, 1, 5, 7],
                                 [2, 1, 9, 8, 5, 7, 4, 3, 6],
                                 [7, 4, 5, 3, 1, 6, 8, 9, 2]],
                                 [[0, 2, 3, 6, 7, 8, 9, 0, 5],
                                  [5, 8, 4, 2, 0, 9, 7, 6, 1],
                                  [9, 6, 7, 1, 4, 5, 3, 2, 8],
                                  [3, 7, 2, 4, 6, 1, 5, 8, 9],
                                  [6, 9, 1, 5, 8, 3, 2, 7, 4],
                                  [4, 5, 8, 7, 9, 2, 6, 1, 3],
                                  [8, 3, 6, 9, 2, 4, 1, 5, 7],
                                  [2, 1, 9, 8, 5, 7, 4, 3, 6],
                                  [7, 4, 5, 3, 1, 6, 8, 9, 2]])

        self.game._filled = 80
        self.game.insert_number(0)
        self.assertEqual(self.game._filled, 79)

    def test_insert_number_to_complete(self):
        self.game._grid = Sudoku(0, [[0, 2, 3, 6, 7, 8, 9, 4, 5],
                                 [5, 8, 4, 2, 3, 9, 7, 6, 1],
                                 [9, 6, 7, 1, 4, 5, 3, 2, 8],
                                 [3, 7, 2, 4, 6, 1, 5, 8, 9],
                                 [6, 9, 1, 5, 8, 3, 2, 7, 4],
                                 [4, 5, 8, 7, 9, 2, 6, 1, 3],
                                 [8, 3, 6, 9, 2, 4, 1, 5, 7],
                                 [2, 1, 9, 8, 5, 7, 4, 3, 6],
                                 [7, 4, 5, 3, 1, 6, 8, 9, 2]],
                                 [[0, 2, 3, 6, 7, 8, 9, 4, 5],
                                  [5, 8, 4, 2, 3, 9, 7, 6, 1],
                                  [9, 6, 7, 1, 4, 5, 3, 2, 8],
                                  [3, 7, 2, 4, 6, 1, 5, 8, 9],
                                  [6, 9, 1, 5, 8, 3, 2, 7, 4],
                                  [4, 5, 8, 7, 9, 2, 6, 1, 3],
                                  [8, 3, 6, 9, 2, 4, 1, 5, 7],
                                  [2, 1, 9, 8, 5, 7, 4, 3, 6],
                                  [7, 4, 5, 3, 1, 6, 8, 9, 2]])

        self.game._filled = 80
        self.game.insert_number(1)
        self.assertTrue(self.game._complete)

    def test_start_new_game(self):
        self.game.start_new_game()
        counted_filled = 81
        for i in range(9):
            for j in range(9):
                if self.game._grid.grid[i][j] == 0:
                    counted_filled -= 1
        self.assertEqual(self.game._filled, counted_filled)
        self.assertFalse(self.game._complete)

    def test_load_empty_game(self):
        self.game._repository.delete()
        with self.assertRaises(NoSavedGame):
            self.game.load_game()

    def test_load_valid_game(self):
        self.game._repository.delete()
        self.game._grid = Sudoku(0, [[0, 2, 3, 6, 7, 8, 9, 4, 5],
                                 [5, 8, 4, 2, 3, 9, 7, 6, 1],
                                 [9, 6, 7, 1, 4, 5, 3, 2, 8],
                                 [3, 7, 2, 4, 6, 1, 5, 8, 9],
                                 [6, 9, 1, 5, 8, 3, 2, 7, 4],
                                 [4, 5, 8, 7, 9, 2, 6, 1, 3],
                                 [8, 3, 6, 9, 2, 4, 1, 5, 7],
                                 [2, 1, 9, 8, 5, 7, 4, 3, 6],
                                 [7, 4, 5, 3, 1, 6, 8, 9, 2]],
                                 [[0, 2, 3, 6, 7, 8, 9, 4, 5],
                                  [5, 8, 4, 2, 3, 9, 7, 6, 1],
                                  [9, 6, 7, 1, 4, 5, 3, 2, 8],
                                  [3, 7, 2, 4, 6, 1, 5, 8, 9],
                                  [6, 9, 1, 5, 0, 3, 2, 7, 4],
                                  [4, 5, 8, 7, 9, 2, 6, 1, 3],
                                  [8, 3, 6, 9, 2, 4, 1, 5, 7],
                                  [2, 1, 0, 8, 5, 7, 0, 3, 6],
                                  [7, 4, 5, 3, 1, 6, 8, 9, 2]])
        self.game._filled = 80
        self.game.save_game()
        self.game._filled = 5
        self.game.load_game()
        self.assertEqual(self.game._filled, 80)
        self.assertFalse(self.game._complete)
        self.assertEqual(self.game._grid.grid, [[0, 2, 3, 6, 7, 8, 9, 4, 5],
                                                [5, 8, 4, 2, 3, 9, 7, 6, 1],
                                                [9, 6, 7, 1, 4, 5, 3, 2, 8],
                                                [3, 7, 2, 4, 6, 1, 5, 8, 9],
                                                [6, 9, 1, 5, 8, 3, 2, 7, 4],
                                                [4, 5, 8, 7, 9, 2, 6, 1, 3],
                                                [8, 3, 6, 9, 2, 4, 1, 5, 7],
                                                [2, 1, 9, 8, 5, 7, 4, 3, 6],
                                                [7, 4, 5, 3, 1, 6, 8, 9, 2]])
        self.assertEqual(self.game._grid.start,   [[0, 2, 3, 6, 7, 8, 9, 4, 5],
                                                   [5, 8, 4, 2, 3, 9, 7, 6, 1],
                                                   [9, 6, 7, 1, 4, 5, 3, 2, 8],
                                                   [3, 7, 2, 4, 6, 1, 5, 8, 9],
                                                   [6, 9, 1, 5, 0, 3, 2, 7, 4],
                                                   [4, 5, 8, 7, 9, 2, 6, 1, 3],
                                                   [8, 3, 6, 9, 2, 4, 1, 5, 7],
                                                   [2, 1, 0, 8, 5, 7, 0, 3, 6],
                                                   [7, 4, 5, 3, 1, 6, 8, 9, 2]])

    def test_save_game(self):
        self.game._repository.delete()

        self.game._grid = Sudoku(0, [[0, 2, 3, 6, 7, 8, 9, 4, 5],
                                 [5, 8, 4, 2, 3, 9, 7, 6, 1],
                                 [9, 6, 7, 1, 4, 5, 3, 2, 8],
                                 [3, 7, 2, 4, 6, 1, 5, 8, 9],
                                 [6, 9, 1, 5, 8, 3, 2, 7, 4],
                                 [4, 5, 8, 7, 9, 2, 6, 1, 3],
                                 [8, 3, 6, 9, 2, 4, 1, 5, 7],
                                 [2, 1, 9, 8, 5, 7, 4, 3, 6],
                                 [7, 4, 5, 3, 1, 6, 8, 9, 2]],
                                 [[0, 2, 3, 6, 7, 8, 9, 4, 5],
                                  [5, 8, 4, 2, 3, 9, 7, 6, 1],
                                  [9, 6, 7, 1, 4, 5, 3, 2, 8],
                                  [3, 7, 2, 4, 6, 1, 5, 8, 9],
                                  [6, 9, 1, 5, 0, 3, 2, 7, 4],
                                  [4, 5, 8, 7, 9, 2, 6, 1, 3],
                                  [8, 3, 6, 9, 2, 4, 1, 5, 7],
                                  [2, 1, 0, 8, 5, 7, 0, 3, 6],
                                  [7, 4, 5, 3, 1, 6, 8, 9, 2]])
        self.game._filled = 80
        self.game.save_game()
        self.game._filled = 4
        self.game.load_game()
        self.assertEqual(self.game._filled, 80)
        self.assertEqual(self.game._grid.grid, [[0, 2, 3, 6, 7, 8, 9, 4, 5],
                                                [5, 8, 4, 2, 3, 9, 7, 6, 1],
                                                [9, 6, 7, 1, 4, 5, 3, 2, 8],
                                                [3, 7, 2, 4, 6, 1, 5, 8, 9],
                                                [6, 9, 1, 5, 8, 3, 2, 7, 4],
                                                [4, 5, 8, 7, 9, 2, 6, 1, 3],
                                                [8, 3, 6, 9, 2, 4, 1, 5, 7],
                                                [2, 1, 9, 8, 5, 7, 4, 3, 6],
                                                [7, 4, 5, 3, 1, 6, 8, 9, 2]])
        self.assertEqual(self.game._grid.start,  [[0, 2, 3, 6, 7, 8, 9, 4, 5],
                                                  [5, 8, 4, 2, 3, 9, 7, 6, 1],
                                                  [9, 6, 7, 1, 4, 5, 3, 2, 8],
                                                  [3, 7, 2, 4, 6, 1, 5, 8, 9],
                                                  [6, 9, 1, 5, 0, 3, 2, 7, 4],
                                                  [4, 5, 8, 7, 9, 2, 6, 1, 3],
                                                  [8, 3, 6, 9, 2, 4, 1, 5, 7],
                                                  [2, 1, 0, 8, 5, 7, 0, 3, 6],
                                                  [7, 4, 5, 3, 1, 6, 8, 9, 2]])

    def test_save_completed_game(self):
        self.game._complete = True
        self.game.save_game()
        with self.assertRaises(NoSavedGame):
            self.game.load_game()
