from pathlib import Path
from config import DIFFICULTY_FILEPATH


class DifficultyRepository:
    """Pelin vaikeustason tallennuksesta vastaava luokka
    """

    def __init__(self, filepath):
        """Pelin vaikeustason tallennuksesta vastaava luokka.

        Args:
            filepath : absoluuttinen tiedostopolku CSV-tiedostoon, 
            jossa pelin vaikeustaso pidetään tallennettuna.
        """
        self._file_path = filepath

    def _ensure_file_exists(self):
        Path(self._file_path).touch()

    def write(self, difficulty):
        """Metodi, joka tallentaa asetetun vaikeustason.

        Args:
            difficulty (int): Vaikeustaso kokonaislukuna.
        """
        self._ensure_file_exists()

        with open(self._file_path, "w", encoding="utf8") as file:
            file.write("difficulty;" + str(difficulty))

    def load(self):
        """Metodi, joka lukee tiedostosta vaikeustason.

        Returns:
            difficulty : vaikeustaso. Jos tallennettuna ei ole mitään,
            palauttaa None, muuten kokonaislukuna vaikeustason.
        """
        self._ensure_file_exists()

        difficulty = None
        with open(self._file_path, encoding="utf8") as file:
            for row in file:
                row_elements = row.strip().split(";")
                if row_elements[0] == "difficulty":
                    difficulty = int(row_elements[1])

        return difficulty


difficulty_repository = DifficultyRepository(DIFFICULTY_FILEPATH)
