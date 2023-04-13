from entities.sudoku import Sudoku


class GameGrid:
    def __init__(self, grid: list, solved: list):
        self._grid = Sudoku(grid, solved)
        self._pos = [0, 0]
        self._filled = 81
        for i in range(9):
            for j in range(9):
                if grid[i][j]==0:
                    self._filled -= 1

    def get_pos(self):
        return tuple(self._pos)

    def move_pos(self, move: str):
        x, y = self.get_pos()
        if move == 'up' and y > 0:
            self._pos[1] -= 1
        elif move == 'down' and y < 8:
            self._pos[1] += 1
        elif move == 'left' and x > 0:
            self._pos[0] -= 1
        elif move == 'right' and x < 8:
            self._pos[0] += 1

    def insert_number(self, number: int):
        if 0 <= number < 10:
            x, y = self.get_pos()
            current_number = self._grid.get_current_number(x, y)
            change = self._grid.insert_number(x, y, number)
            if change:
                if current_number == 0 and number >0:
                    self._filled += 1
                elif current_number != 0 and number == 0:
                    self._filled -= 1                      
        if self._filled == 81:
            return self.check_if_complete()
        return False

    def check_if_complete(self):
        return self._grid.check_if_complete()
