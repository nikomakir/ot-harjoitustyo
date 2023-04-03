import unittest
from entities.sudoku import Sudoku

class TestSudoku(unittest.TestCase):
    def setUp(self):
        self.grid = Sudoku([[0,2,0],[0,5,0],[0,0,9]],[[1,2,3],[4,5,6],[7,8,9]])

    def test_inserting_valid_number(self):
        self.grid._insert_number(0,1,4)
        self.assertEqual(self.grid._grid[1][0],4)
    
    def test_inserting_into_starting_square(self):
        self.grid._insert_number(1,0,8)
        self.assertEqual(self.grid._grid[0][1],2)

    def test_changing_grid_doesnt_change_starting_grid(self):
        self.grid._insert_number(0,1,4)
        self.assertEqual(self.grid._start[1][0],0)

    def test_completing_grid_returns_true(self):
        for i in range(3):
            for j in range(3):
                if self.grid._grid[i][j] != self.grid._solved[i][j]:
                    self.grid._insert_number(j,i,self.grid._solved[i][j])
        self.assertTrue(self.grid._check_if_complete())
    
    def test_checking_if_complete_when_not_complete_return_false(self):
        self.assertFalse(self.grid._check_if_complete())