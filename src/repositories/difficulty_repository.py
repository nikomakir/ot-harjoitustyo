from pathlib import Path
from config import DIFFICULTY_FILEPATH


class DifficultyRepository:
    def __init__(self, filepath):
        self._file_path = filepath

    def _ensure_file_exists(self):
        Path(self._file_path).touch()

    def write(self, difficulty):
        self._ensure_file_exists()

        with open(self._file_path, "w", encoding="utf8") as file:
            file.write("difficulty;" + str(difficulty))

    def load(self):
        self._ensure_file_exists()

        difficulty = None
        with open(self._file_path, encoding="utf8") as file:
            for row in file:
                row_elements = row.strip().split(";")
                if row_elements[0] == "difficulty":
                    difficulty = int(row_elements[1])

        return difficulty
    
difficulty_repository = DifficultyRepository(DIFFICULTY_FILEPATH)

