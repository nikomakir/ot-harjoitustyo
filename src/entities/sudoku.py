class Sudoku:
    def  __init__(self,grid:list,solved:list):
        self._grid = grid
        self._start = [row[:] for row in grid]
        self._solved = solved
    
    def _insert_number(self,x,y,number):
        if self._start[y][x] != 0:
            return
        self._grid[y][x] = number

    def _check_if_complete(self):
        return self._grid==self._solved
    