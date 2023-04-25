from entities.sudoku import Sudoku
from repositories.sudoku_repository import sudoku_repository as default_sudoku_repository


class NoSavedGame(Exception):
    pass


class GameService:
    def __init__(self, sudoku_repository=default_sudoku_repository):
        self._grid = None
        self._pos = [0, 0]
        self._complete = False
        self._repository = sudoku_repository
        self._filled = None

    def start_new_game(self, difficulty=50):
        self._grid = Sudoku(difficulty)
        filled = 81
        for i in range(9):
            for j in range(9):
                if self._grid.grid[i][j] == 0:
                    filled -= 1
        self._filled = filled
        self._complete = False

    def get_pos(self):
        return tuple(self._pos)

    def move_pos(self, move: str):
        if self._complete:
            return
        x, y = self.get_pos()            # pylint: disable=invalid-name
        if move == 'up' and y > 0:
            self._pos[1] -= 1
        elif move == 'down' and y < 8:
            self._pos[1] += 1
        elif move == 'left' and x > 0:
            self._pos[0] -= 1
        elif move == 'right' and x < 8:
            self._pos[0] += 1

    def insert_number(self, number: int):
        if self._complete:
            return
        if 0 <= number < 10:
            x, y = self.get_pos()              # pylint: disable=invalid-name
            current_number = self._grid.get_current_number(x, y)
            change = self._grid.insert_number(x, y, number)
            if change:
                if current_number == 0 and number > 0:
                    self._filled += 1
                elif current_number != 0 and number == 0:
                    self._filled -= 1
        if self._filled == 81:
            self._complete = self.check_if_complete()

    def check_if_complete(self):
        return self._grid.check_if_complete()

    def load_game(self):
        grid, start, filled = self._repository.load()

        if (len(grid) or len(start)) == 0:
            raise NoSavedGame('No saved game available!')

        self._grid = Sudoku(0, grid, start)
        self._filled = filled
        self._complete = False

    def save_game(self):
        if not self._complete:
            self._repository.write(
                self._filled, self._grid.grid, self._grid.start)
        else:
            self._repository.delete()


game_service = GameService()
