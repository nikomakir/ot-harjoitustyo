import pygame

class GameLoop:
    def __init__(self,grid,renderer,event_queue):
        self._grid = grid
        self._renderer = renderer
        self._event_queue = event_queue

    def start(self):
        self._render()
        while True:
            if self._hande_events()==False:
                break
    
    def _hande_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                return False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT: 
                    self._grid._move_pos('left')
                    self._render()
                if event.key==pygame.K_UP: 
                    self._grid._move_pos('up')
                    self._render()
                if event.key==pygame.K_DOWN: 
                    self._grid._move_pos('down')
                    self._render()
                if event.key==pygame.K_RIGHT: 
                    self._grid._move_pos('right')
                    self._render()
                if event.key==pygame.K_1: 
                    self._grid._insert_number(1)
                    self._render()
                if event.key==pygame.K_2: 
                    self._grid._insert_number(2)
                    self._render()
                if event.key==pygame.K_3: 
                    self._grid._insert_number(3)
                    self._render()
                if event.key==pygame.K_4: 
                    self._grid._insert_number(4)
                    self._render()
                if event.key==pygame.K_5:
                    self._grid._insert_number(5)
                    self._render()
                if event.key==pygame.K_6: 
                    self._grid._insert_number(6)
                    self._render()
                if event.key==pygame.K_7: 
                    self._grid._insert_number(7)
                    self._render()
                if event.key==pygame.K_8: 
                    self._grid._insert_number(8)
                    self._render()
                if event.key==pygame.K_9: 
                    self._grid._insert_number(9)
                    self._render()
                if event.key==pygame.K_DELETE or event.key==pygame.K_BACKSPACE:
                    self._grid._insert_number(0)
                    self._render()
            
    def _render(self):
        self._renderer.render()