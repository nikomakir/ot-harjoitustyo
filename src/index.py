import pygame
from service.grid import GameGrid
from ui.renderer import Renderer
from eventqueue import EventQueue
from gameloop import GameLoop
from entities.sudoku import Sudoku

grid = [
[3,0,5,4,0,2,0,6,0],
[4,9,0,7,6,0,1,0,8],
[6,0,0,1,0,3,2,4,5],
[0,0,3,9,0,0,5,8,0],
[9,6,0,0,5,8,7,0,3],
[0,8,1,3,0,4,0,9,2],
[0,5,0,6,0,1,4,0,0],
[2,0,0,5,4,9,0,7,0],
[1,4,9,0,0,7,3,0,6]    
]
solved = [
[3,1,5,4,8,2,9,6,7],
[4,9,2,7,6,5,1,3,8],
[6,7,8,1,9,3,2,4,5],
[7,2,3,9,1,6,5,8,4],
[9,6,4,2,5,8,7,1,3],
[5,8,1,3,7,4,6,9,2],
[8,5,7,6,3,1,4,2,9],
[2,2,6,5,4,9,8,7,1],
[1,4,9,8,2,7,3,5,6]    
]
def main():
    width = 550
    display = pygame.display.set_mode((width,width))
    pygame.display.set_caption("Sudoku")

    game_grid = GameGrid(grid,solved)
    renderer = Renderer(display,game_grid)
    event_queue = EventQueue()
    game_loop = GameLoop(game_grid,renderer,event_queue)
    
    pygame.init()
    game_loop.start()


if __name__=="main":
    main()
