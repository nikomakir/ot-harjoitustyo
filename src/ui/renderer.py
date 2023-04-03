import pygame
from service.grid import GameGrid

class Renderer:
    def __init__(self,display,grid:GameGrid):
        self._display = display
        self._grid = grid
        self._background_color = (251,247,245)
        self._starting_font = pygame.font.SysFont('Comic Sans MS', 35)
        self._original_grid_color = (52,31,151)

    def render(self):
        self._display.fill(self._background_color)

        for i in range(10):
            if i%3==0:
                pygame.draw.line(self._display,(0,0,0),(50+50*i,50),(50+50*i,500),4)
                pygame.draw.line(self._display,(0,0,0),(50,50+50*i),(500,50+50*i),4)
            pygame.draw.line(self._display,(0,0,0),(50+50*i,50),(50+50*i,500),2)
            pygame.draw.line(self._display,(0,0,0),(50,50+50*i),(500,50+50*i),2)
        pygame.display.update()

        for i in range(9):
            for j in range(9):
                if 0<self._grid._grid._start[i][j]<10:
                    value = self._starting_font.render(str(self._grid._grid._start[i][j]),True,self._original_grid_color)
                    self._display.blit(value,((j+1)*50+15,(i+1)*50))
        pygame.display.update()
