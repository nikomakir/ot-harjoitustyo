import unittest
from repositories.sudoku_repository import sudoku_repository


class TestSudokuRepository(unittest.TestCase):
    def setUp(self):
        sudoku_repository.delete()
        self.difficulty = 20
        self.filled = 80
        self.grid = [[1, 2, 3, 6, 7, 8, 9, 4, 5],
                     [5, 8, 4, 2, 3, 9, 7, 6, 1],
                     [9, 6, 7, 1, 4, 5, 3, 2, 8],
                     [3, 7, 2, 4, 6, 1, 5, 8, 9],
                     [6, 9, 1, 5, 8, 3, 2, 7, 4],
                     [4, 5, 8, 7, 9, 2, 6, 1, 3],
                     [8, 3, 6, 9, 2, 4, 1, 5, 7],
                     [2, 1, 9, 8, 5, 7, 4, 3, 6],
                     [7, 4, 5, 3, 1, 6, 8, 9, 2]]

        self.start = [[0, 2, 3, 6, 7, 8, 9, 4, 5],
                      [5, 8, 4, 2, 3, 9, 7, 6, 1],
                      [9, 6, 7, 1, 4, 5, 3, 2, 8],
                      [3, 7, 2, 4, 6, 1, 5, 8, 9],
                      [6, 9, 1, 5, 8, 3, 2, 7, 4],
                      [4, 5, 8, 7, 9, 2, 6, 1, 3],
                      [8, 3, 6, 9, 2, 4, 1, 5, 7],
                      [2, 1, 9, 8, 5, 7, 4, 3, 6],
                      [7, 4, 5, 3, 1, 6, 8, 9, 2]]

    def test_write(self):
        sudoku_repository.write(
            self.difficulty, self.filled, self.grid, self.start)
        grid, start, filled, difficulty = sudoku_repository.load()
        self.assertEqual(filled, self.filled)
        self.assertEqual(grid, self.grid)
        self.assertEqual(start, self.start)
        self.assertEqual(difficulty, self.difficulty)

    def test_load(self):
        sudoku_repository.write(
            self.difficulty, self.filled, self.grid, self.start)
        grid, start, filled, difficulty = sudoku_repository.load()
        self.assertEqual(filled, self.filled)
        self.assertEqual(difficulty, self.difficulty)
        self.assertEqual(len(grid), 9)
        self.assertEqual(len(grid[0]), 9)
        self.assertEqual(len(grid[1]), 9)
        self.assertEqual(len(grid[2]), 9)
        self.assertEqual(len(grid[3]), 9)
        self.assertEqual(len(grid[4]), 9)
        self.assertEqual(len(grid[5]), 9)
        self.assertEqual(len(grid[6]), 9)
        self.assertEqual(len(grid[7]), 9)
        self.assertEqual(len(grid[8]), 9)
        self.assertEqual(len(start), 9)
        self.assertEqual(len(start[0]), 9)
        self.assertEqual(len(start[1]), 9)
        self.assertEqual(len(start[2]), 9)
        self.assertEqual(len(start[3]), 9)
        self.assertEqual(len(start[4]), 9)
        self.assertEqual(len(start[5]), 9)
        self.assertEqual(len(start[6]), 9)
        self.assertEqual(len(start[7]), 9)
        self.assertEqual(len(start[8]), 9)
        self.assertEqual(grid, self.grid)
        self.assertEqual(start, self.start)

    def test_delete(self):
        sudoku_repository.write(
            self.difficulty, self.filled, self.grid, self.start)
        sudoku_repository.delete()
        grid, start, filled, difficulty = sudoku_repository.load()
        self.assertEqual(filled, 0)
        self.assertEqual(difficulty, 0)
        self.assertEqual(len(grid), 0)
        self.assertEqual(len(start), 0)
