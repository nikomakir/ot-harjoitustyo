from dokusan import generators
import numpy as np

class Sudoku:
    def __init__(self, difficulty):
        grid = np.array(list(str(generators.random_sudoku(avg_rank=difficulty)))).reshape(9,9)
        self._grid = np.asarray(grid,dtype=int)
        self._start = np.copy(self._grid)

    def insert_number(self, x, y, number):
        if self._start[y][x] != 0:
            return False
        self._grid[y][x] = number
        return True

    def check_if_complete(self):
        for i in range(9):
            seen_in_rows = set()
            seen_in_columns = set()
            for j in range(9):
                number = self._grid[i][j]
                if number == 0 or number in seen_in_rows:
                    return False
                seen_in_rows.add(number)
                number = self._grid[j][i]
                if number in seen_in_columns:
                    return False
                seen_in_columns.add(number)

        for l in range(0,7,3):
            for k in range(0,7,3):
                seen_in_squares = set()
                for i in range(3):
                    for j in range(3):
                        number = self._grid[i+l][j+k]
                        if number in seen_in_squares:
                            return False
                        seen_in_squares.add(number)
        return True
                
    
    def get_current_number(self, x, y):
        return self._grid[y][x]
