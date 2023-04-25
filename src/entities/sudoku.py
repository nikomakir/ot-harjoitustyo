from dokusan import generators
import numpy as np


class Sudoku:
    def __init__(self, difficulty, grid=None, start=None):
        self.grid = grid
        self.start = start
        if grid is None:
            self._initialize_grid(difficulty)

    def _initialize_grid(self, difficulty):
        grid = np.array(
            list(str(generators.random_sudoku(avg_rank=difficulty)))).reshape(9, 9)
        self.grid = np.asarray(grid, dtype=int)
        self.start = np.copy(self.grid)

    def insert_number(self, x, y, number):  # pylint: disable=invalid-name
        if self.start[y][x] != 0:
            return False
        self.grid[y][x] = number
        return True

    def check_if_complete(self):
        for i in range(9):
            seen_in_rows = set()
            seen_in_columns = set()
            for j in range(9):
                number = self.grid[i][j]
                if number == 0 or number in seen_in_rows:
                    return False
                seen_in_rows.add(number)
                number = self.grid[j][i]
                if number in seen_in_columns:
                    return False
                seen_in_columns.add(number)
        return True

    def get_current_number(self, x, y):  # pylint: disable=invalid-name
        return self.grid[y][x]
