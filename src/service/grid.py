from entities.sudoku import Sudoku

class GameGrid:
    def __init__(self,grid:list,solved:list):
        self._grid = Sudoku(grid,solved)
        self._pos = [0,0]

    def _get_pos(self):
        return tuple(self._pos)
    
    def _move_pos(self,move:str):
        x,y = self._get_pos()
        if move=='up' and y>0:
            self._pos[1] -= 1
        elif move=='down' and y<8:
            self._pos[1] += 1
        elif move=='left' and x>0:
            self._pos[0] -= 1
        elif move=='right' and x<8:
            self._pos[0] += 1

    def _insert_number(self,number:int):
        x,y = self._get_pos()
        self._grid._insert_number(x,y,number)

    def _check_if_complete(self):
        return self._grid._check_if_complete()

    