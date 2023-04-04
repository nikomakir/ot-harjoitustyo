import pygame
from service.grid import GameGrid

class Renderer:
    def __init__(self,display,grid:GameGrid):
        self._display = display
        self._grid = grid
        self._background_color = (251,247,245)
        self._starting_font = pygame.font.SysFont('Comic Sans MS', 35)
        self._original_grid_color = (52,31,151)
        self._number_color = (0,0,0)
        self._choice_color = (255,200,200)

    def render(self):
        self._display.fill(self._background_color)
        x,y = self._grid._get_pos()
        pygame.draw.rect(self._display,self._choice_color,pygame.Rect(x*50+50,y*50+50,50,50))
        pygame.display.update()

        for i in range(10):
            if i%3==0:
                pygame.draw.line(self._display,(0,0,0),(50+50*i,50),(50+50*i,500),5)
                pygame.draw.line(self._display,(0,0,0),(50,50+50*i),(500,50+50*i),5)
            pygame.draw.line(self._display,(0,0,0),(50+50*i,50),(50+50*i,500),2)
            pygame.draw.line(self._display,(0,0,0),(50,50+50*i),(500,50+50*i),2)
        pygame.display.update()

        for i in range(9):
            for j in range(9):
                if 0<self._grid._grid._start[i][j]:
                    value = self._starting_font.render(str(self._grid._grid._start[i][j]),True,self._original_grid_color)
                    self._display.blit(value,((j+1)*50+15,(i+1)*50))
                if self._grid._grid._grid[i][j] != self._grid._grid._start[i][j]:
                    value = self._starting_font.render(str(self._grid._grid._grid[i][j]),True,self._number_color)
                    self._display.blit(value,((j+1)*50+15,(i+1)*50))
        pygame.display.update()
