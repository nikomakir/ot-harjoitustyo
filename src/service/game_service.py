from entities.sudoku import Sudoku
from repositories.sudoku_repository import (sudoku_repository as
                                            default_sudoku_repository)
from repositories.difficulty_repository import (difficulty_repository as
                                                default_difficulty_repository)


class NoSavedGame(Exception):
    pass


class GameService:
    """Sovelluslogiikasta vastaava luokka.
    """

    def __init__(self, sudoku_repository=default_sudoku_repository,
                 difficulty_repository=default_difficulty_repository):
        """Sovelluslogiikasta vastaava luokka.

        Attributes:
            grid : peliruudukko. Alussa arvona None.
            pos : valittuna oleva ruutu muodossa x, y, missä x on 
            vaakatason ja y pystytason koordinaatit
            complete : Boolean arvo, joka kuvastaa pelin tilaa (kesken/valmis)
            repository: Tallentamisesta vastaava luokka SudokuRepository
            difficulty_repository: Pelin vaikeustason tallennuksesta ja lataamisesta vastaava luokka
            filled : kaikista sudokuruudukon 81 luvusta ne luvut, jotka on 
            kyseisenä hetkenä täytetty. 
            current_difficulty : nykyisen pelin vaikeustaso

        Args:
            sudoku_repository (optional): Tallentamisesta vastaava luokka SudokuRepository
            difficulty_repository (optional): Vaikeustason tallentamisesta vastaava luokka 
            DifficultyRepository
        """
        self._grid = None
        self._pos = [0, 0]
        self._complete = False
        self._repository = sudoku_repository
        self.difficulty_repository = difficulty_repository
        self._filled = None
        self.current_difficulty = 0

    def _get_difficulty(self):
        """Metodi, joka hakee tiedostosta asetetun vaikeustason hyödyntäen
        DifficultyRepository luokan metodia load().

        Raises:
            NoSavedGame: Nostaa poikkeuksen, jos ei ole mitään tallennettuna.

        Returns:
            difficulty: vaikeustaso kokonaislukuna
        """
        difficulty = self.difficulty_repository.load()
        if difficulty is None:
            raise NoSavedGame('No difficulty set!')
        return difficulty

    def save_difficulty(self, difficulty):
        """Metodi, joka tallentaa asetetun vaikeustason käyttäen DifficultyRepositoryn
        metodia write().

        Args:
            difficulty (int): vaikeustaso kokonaislukuna
        """
        self.difficulty_repository.write(difficulty)

    def start_new_game(self):
        """Metodi, joka aloittaa uuden pelin. Lataa asetetun vaikeustason, jos ei ole asetettu,
        niin asettaa oletusarvoisesti luvun 20. Tätä tarvitaan Sudoku -luokan luomisessa. 
        Luo Sudoku -luokan ja asettaa sen
        self._grid attribuuttiin. Asettaa oikeat self._filled ja self._current_difficulty 
        attribuuttien arvot ja  asettaa self._complete arvon takaisin False, 
        jos viimeksi pelattiin valmiiksi.
        """
        try:
            difficulty = self._get_difficulty()
        except NoSavedGame:
            difficulty = 20

        self._grid = Sudoku(difficulty)
        filled = 81
        for i in range(9):
            for j in range(9):
                if self._grid.grid[i][j] == 0:
                    filled -= 1
        self._filled = filled
        self.current_difficulty = difficulty
        self._complete = False

    def get_pos(self):
        return tuple(self._pos)

    def move_pos(self, move: str):
        """Metodi, joka liikuttaa valittua ruutua eli muuttaa self._pos attribuutin
        arvoa, ellei peli ole valmis. Pitää myöskin valitun ruudun peliruudukon raameissa.

        Args:
            move (str): Liike merkkijonona. Saadaan käyttöliittymältä tapahtumien käsittelyn 
            yhteydessä.
        """
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
        """Metodi, joka syöttää annetun luvun valittuna olevaan ruutuun, ellei
        peli ole valmis ja annettu luku halutulla välillä 0-9. Jos syöton jälkeen
        attribuutti self._filled on 81, päivittää self._complete attribuutin arvon.

        Args:
            number (int): Syötetty luku. Sudokussa luvut 1-9 ovat sallittuja
            ja luku 0 kuvastaa tässä tyhjää ruutua.
        """
        if self._complete:
            return
        if 0 <= number < 10:
            x, y = self.get_pos()              # pylint: disable=invalid-name
            current_number = self._grid.get_current_number(x, y)
            if self._grid.insert_number(x, y, number):
                if current_number == 0 and number > 0:
                    self._filled += 1
                elif current_number != 0 and number == 0:
                    self._filled -= 1
        if self._filled == 81:
            self._complete = self.check_if_complete()

    def check_if_complete(self):
        """Metodi, joka tarkistaa, onko ruudukko syötetty oikein. Kutsuu Sudoku 
        -luokan metodia check_if_complete().

        Returns:
            Boolean: True/False sen mukaan, onko peli oikein syötetty ja siten valmis.
        """
        return self._grid.check_if_complete()

    def load_game(self):
        """Metodi, joka lataa pelin. Kutsuu SudokuRepository -luokan
        metodia load() ja syöttää arvot muuttujiin grid, start, filled ja difficulty.
        Näillä luo uuden Sudoku -luokan olion self._grid attribuuttiin ja päivittää 
        self._filled, self._current_difficulty ja self._complete attribuutit.
        Jos grid tai start on tyjiä, peliä ei ole tallennettu ja nostaa tästä poikkeuksen.


        Raises:
            NoSavedGame: Poikkeus, jos peliä ei ole tallennettu.
        """
        grid, start, filled, difficulty = self._repository.load()

        if (len(grid) or len(start)) == 0:
            raise NoSavedGame('No saved game available!')

        self._grid = Sudoku(0, grid, start)
        self._filled = filled
        self.current_difficulty = difficulty
        self._complete = False

    def save_game(self):
        """Tallentamisesta vastaava metodi. Kutsuu SudokuRepository -luokan 
        metodia write() omilla attribuuttien self._current_difficulty, self._filled 
        ja self._grid Sudoku luokan attributtien grid ja start arvoilla, jos peli on kesken.
        Mikäli peli on valmis, metodi kutsuu SudokuRepository -luokan metodia delete(), 
        joka tyhjentää tiedot. 
        """
        if not self._complete:
            self._repository.write(self.current_difficulty,
                                   self._filled, self._grid.grid, self._grid.start)
        else:
            self._repository.delete()


game_service = GameService()
