from pathlib import Path
from config import SUDOKU_FILEPATH


class SudokuRepository:
    def __init__(self, file_path):
        self._file_path = file_path

    def _ensure_file_exists(self):
        Path(self._file_path).touch()

    def write(self, filled, grid, start):
        self._ensure_file_exists()

        with open(self._file_path, "w", encoding="utf8") as file:
            file.write("filled;" + str(filled) + "\n")
            file.write("grid\n")
            for row in grid:
                to_be_written = ""
                for number in row:
                    to_be_written += str(number) + ";"
                file.write(to_be_written[:-1] + "\n")

            file.write("start\n")
            for row in start:
                to_be_written = ""
                for number in row:
                    to_be_written += str(number) + ";"
                file.write(to_be_written[:-1] + "\n")

    def load(self):
        self._ensure_file_exists()

        grid = []
        start = []
        filled = None

        with open(self._file_path, encoding="utf8") as file:
            grid_to_append = False
            for row in file:
                if row.startswith("filled"):
                    filled = int(row.strip().split(";")[1])
                    continue
                if row.startswith("grid"):
                    grid_to_append = True
                    continue
                if row.startswith("start"):
                    grid_to_append = False
                    continue
                row.replace("\n", "")
                numbers = row.split(";")
                if grid_to_append:
                    grid.append([int(number) for number in numbers])
                else:
                    start.append([int(number) for number in numbers])

        return grid, start, filled

    def delete(self):
        self.write(0, [], [])


sudoku_repository = SudokuRepository(SUDOKU_FILEPATH)
