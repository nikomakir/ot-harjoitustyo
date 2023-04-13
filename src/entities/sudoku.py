class Sudoku:
    def __init__(self, grid: list, solved: list):
        self._grid = grid
        self._start = [row[:] for row in grid]
        self._solved = solved

    def insert_number(self, x, y, number):
        if self._start[y][x] != 0:
            return False
        self._grid[y][x] = number
        return True

    def check_if_complete(self):
        return self._grid == self._solved
    
    def get_current_number(self, x, y):
        return self._grid[y][x]
