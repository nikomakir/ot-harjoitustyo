from pathlib import Path
from config import SUDOKU_FILEPATH


class SudokuRepository:
    """Sudoku -ruudukon tallentamisesta vastaava luokka.
    """

    def __init__(self, file_path):
        """Sudoku -ruudukon tallentamisesta vastaava luokka.

        Args:
            file_path : absoluuttinen tiedostopolku CSV -tiedostoon, jonne tiedot tallennetaan. 
        """
        self._file_path = file_path

    def _ensure_file_exists(self):
        Path(self._file_path).touch()

    def write(self, difficulty, filled, grid, start):
        """Tallentamisesta vastaava metodi.Tallentaa ensimmäiselle riville difficulty 
        ja filled arvon ja  toiselta riviltä lähtien peliruudukon matriisin rivi kerrallaan. 
        Väleissä rivi tekstiä, joka kertoo mistä tiedosta on kyse.

        Args:
            difficulty (int) : Tallennettavan pelin vaikeustaso.
            filled (int): GameService -luokan attribuutti self._filled arvo.
            grid (list): Peliruudukko listana.
            start (list): Aloitusruudukko listana.
        """
        self._ensure_file_exists()

        with open(self._file_path, "w", encoding="utf8") as file:
            file.write("difficulty;" + str(difficulty) +
                       ";filled;" + str(filled) + "\n")
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
        """Tallennetun pelin lataamisesta eli lukemisesta vastaava metodi.
        Aluksi varmistetaan, että tiedosto on olemassa, minkä jälkeen luetaan
        tiedosto rivi kerrallaan ja täytetään tiedot muuttujiin grid, start ja filled.

        Returns:
            tuple: peli- ja aloitusruudukko listana ja GameService luokan tarvitsema self._filled 
            arvo kokonaislukuna. 
        """
        self._ensure_file_exists()

        grid = []
        start = []
        filled = 0
        difficulty = 0

        with open(self._file_path, encoding="utf8") as file:
            start_to_append = False
            for row in file:
                if row.startswith("difficulty"):
                    data = row.strip().split(";")
                    difficulty = int(data[1])
                    filled = int(data[3])
                    continue
                if row.startswith("grid"):
                    continue
                if row.startswith("start"):
                    start_to_append = True
                    continue
                numbers = row.strip().split(";")
                if start_to_append:
                    start.append([int(number) for number in numbers])
                else:
                    grid.append([int(number) for number in numbers])

        return grid, start, filled, difficulty

    def delete(self):
        """Metodi, joka tyhjentää tiedoston tiedot. Kutsuu metodia write()
        tyhjillä arvoilla.
        """
        self.write(0, 0, [], [])


sudoku_repository = SudokuRepository(SUDOKU_FILEPATH)
