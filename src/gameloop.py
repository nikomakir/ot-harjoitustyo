import pygame

class GameLoop:
    def __init__(self,grid,renderer,event_queue):
        self._grid = grid
        self._renderer = renderer
        self._event_queue = event_queue

    def start(self):
        while True:
            if self._hande_events()==False:
                break
            self._render()

    def _hande_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                return False
            
    def _render(self):
        self._renderer.render()