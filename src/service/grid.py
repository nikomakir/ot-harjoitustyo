from entities.sudoku import Sudoku


class GameGrid:
    def __init__(self, grid: list, solved: list):
        self._grid = Sudoku(grid, solved)
        self._pos = [0, 0]

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
            self._grid.insert_number(x, y, number)

    def check_if_complete(self):
        return self._grid.check_if_complete()
