from dokusan import generators
import numpy as np


class Sudoku:
    """Sudoku ruudukkoa kuvaava luokka. Luokalle voi antaa valmiit matriisit
      tai oletusarvoisesti luo uuden ruudukon 
       dokusan kirjaston avulla.
       Attributes:
        grid: matriisi, joka kuvaa täytettävää Sudoku ruudukkoa (oletusarvona None)
        start: matriisi, joka kuvaa aloitustilassa ollutta ruudukkoa (oletusarvona None)
    """

    def __init__(self, difficulty, grid=None, start=None):
        """Luokan konstruktori, joka luo oletusavoisesti uuden Sudoku-ruudukon 
        dokusan kirjaston avulla. 

        Args:
            difficulty (int): vaikeustaso kokonaislukuna
            grid (list, optional): Matriisi, joka kuvaa täytettävää ruudukkoa. 
            Oletusarvona None.
            start (list, optional): Matriisi, joka kuvaa aloitustilassa ollutta ruudukkoa. 
            Oletusarvona None.
        """
        self.grid = grid
        self.start = start
        if grid is None:
            self._initialize_grid(difficulty)

    def _initialize_grid(self, difficulty):
        """Metodi, joka luo uuden sudoku ruudukon dokusan kirjaston avulla. 
        generators moduuli palauttaa ruudukon merkkijonona,
        joka muutetaan numpy kirjaston avulla 9x9 ruudukoksi,
        eli siis 9 riviä sisältäväksi listaksi, jonka kullakin rivillä 
        on 9 alkiota. Tämän jälkeen vielä muutetaan luokan attribuutti self.grid 
        viittaamaan kyseiseen tietorakenteeseen 
        tulkiten alkiot kokonaislukuina. Nyt voidaan käsitellä taulukkoa 
        kuten python listaa. Lopuksi vielä tallennetaan
        luokan attribuuttiin self.start kopio ruudukosta. 


        Args:
            difficulty (int): vaikeustasoa kuuvaava kokonaisluku
        """
        grid = np.array(
            list(str(generators.random_sudoku(avg_rank=difficulty)))).reshape(9, 9)
        self.grid = np.asarray(grid, dtype=int)
        self.start = np.copy(self.grid)

    def insert_number(self, x, y, number):  # pylint: disable=invalid-name
        """Numeron täyttämisestä vastaava metodi.

        Args:
            x (int): Ruudukon vaakatasolla oleva koordinaatti
            y (int): Ruudukon pystytasolla oleva koordinaatti
            number (int): Syötettävä luku

        Returns:
            Boolean: Jos täytettävä ruutu on jo valmiiksi aloituksessa täytetty ruutu,
              palautetaan False. Mikäli ei ollut, niin
            muutetaan ruutua kuvaava listan alkio syötettäväksi luvuksi 
            ja palautetaan True.
        """
        if self.start[y][x] != 0:
            return False
        self.grid[y][x] = number
        return True

    def check_if_complete(self):
        """Tarkistaa, onko ruudukko oikein täytetty. Tarkistuksessa käytetään hyödyksi
          hajautustaulua ja käydään läpi samaan aikaan rivit ja sarakkeet.

        Returns:
            Boolean: Palauttaa False, jos ei ole oikein täytetty, muuten True.
        """
        for i in range(9):
            seen_in_rows = set()
            seen_in_columns = set()
            for j in range(9):
                number = self.grid[i][j]
                if number == 0 or number in seen_in_rows:
                    return False
                seen_in_rows.add(number)
                number = self.grid[j][i]
                if number in seen_in_columns:
                    return False
                seen_in_columns.add(number)
        return True

    def get_current_number(self, x, y):  # pylint: disable=invalid-name
        """Metodi, joka palauttaa ruudukon tietyn ruudun luvun listalta.

        Args:
            x (int): Ruudukon vaakarivin koordinaattia kuvaava luku.
            y (int): Ruudukon pystyrivin koordinaattia kuvaava luku.

        Returns:
            int: Palauttaa kyseisen kohdan luvun, joka on tallennettu matriisiin.
        """
        return self.grid[y][x]
