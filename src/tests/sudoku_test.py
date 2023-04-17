import unittest
from entities.sudoku import Sudoku


class TestSudoku(unittest.TestCase):
    """
    Tämä testaa vain Sudoku -luokan toiminnallisuutta. 
    dokusan ja numpy kirjaston toimintoja ei testata erikseen.
    
    """
    def setUp(self):
        self.grid =  Sudoku(50)
        self.grid._grid =  [[0, 2, 0], [0, 5, 0], [0, 0, 9]]
        self.grid._start =  [row[:] for row in self.grid._grid]

    def test_inserting_valid_number(self):
        self.grid.insert_number(0, 1, 4)
        self.assertEqual(self.grid._grid[1][0], 4)

    def test_inserting_valid_number_returns_true(self):
        self.assertTrue(self.grid.insert_number(0, 1, 4))

    def test_inserting_into_starting_square(self):
        self.grid.insert_number(1, 0, 8)
        self.assertEqual(self.grid._grid[0][1], 2)
    
    def test_inserting_into_starting_square_returns_false(self):
        self.assertFalse(self.grid.insert_number(1, 0, 8))

    def test_completing_grid_returns_true(self):
        self.grid._grid = [[1,2,3,6,7,8,9,4,5],
                           [5,8,4,2,3,9,7,6,1],
                           [9,6,7,1,4,5,3,2,8],
                           [3,7,2,4,6,1,5,8,9],
                           [6,9,1,5,8,3,2,7,4],
                           [4,5,8,7,9,2,6,1,3],
                           [8,3,6,9,2,4,1,5,7],
                           [2,1,9,8,5,7,4,3,6],
                           [7,4,5,3,1,6,8,9,2]]
        self.assertTrue(self.grid.check_if_complete())

    def test_checking_if_complete_when_not_complete_return_false(self):
        self.grid._grid = [[1,2,3,6,7,8,9,4,5],
                           [5,8,4,2,3,9,7,6,1],
                           [9,6,7,1,4,5,3,2,8],
                           [3,7,2,4,6,1,5,8,9],
                           [6,9,1,5,8,3,2,7,4],
                           [4,5,8,7,0,2,6,1,3],
                           [8,3,6,9,2,4,1,5,7],
                           [2,1,9,8,5,7,4,3,6],
                           [7,4,5,3,1,6,8,9,2]]
        self.assertFalse(self.grid.check_if_complete())

    def test_check_if_complete_returns_false_when_row_false(self):
        self.grid._grid = [[1,2,3,6,7,8,9,4,5],
                           [5,8,4,2,3,9,7,6,1],
                           [9,6,7,1,4,5,3,2,8],
                           [3,7,2,4,6,1,5,8,9],
                           [6,9,1,5,8,3,2,7,4],
                           [4,5,8,7,9,2,6,1,3],
                           [8,3,6,9,2,4,1,5,7],
                           [2,1,9,8,5,7,4,3,6],
                           [7,4,5,3,1,6,8,3,2]]
        self.assertFalse(self.grid.check_if_complete())
    
    def test_check_if_complete_returns_false_when_column_false(self):
        self.grid._grid = [[1,2,3,6,7,8,9,4,5],
                           [5,8,4,2,3,9,7,6,1],
                           [9,6,7,1,4,5,3,2,8],
                           [3,7,2,4,6,1,5,8,9],
                           [6,9,1,5,8,3,2,7,4],
                           [4,5,8,7,9,2,6,1,3],
                           [8,3,6,9,2,4,1,5,7],
                           [5,1,9,8,5,7,4,3,6],
                           [7,4,5,3,1,6,8,9,2]]
        self.assertFalse(self.grid.check_if_complete())

    def test_get_current_number_returns_correct(self):
        self.grid._grid = [[1,2,3],[2,5,4]]
        self.assertEqual(self.grid.get_current_number(0,1), 2)