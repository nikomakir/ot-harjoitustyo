import pygame


class GameLoop:
    def __init__(self, service, renderer, event_queue):
        self._service = service
        self._renderer = renderer
        self._event_queue = event_queue

    def start(self):
        self._render()
        while True:
            if self._hande_events() is False:
                break

        self._service.save_game()

    def _hande_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._service.move_pos('left')
                    self._render()
                if event.key == pygame.K_UP:
                    self._service.move_pos('up')
                    self._render()
                if event.key == pygame.K_DOWN:
                    self._service.move_pos('down')
                    self._render()
                if event.key == pygame.K_RIGHT:
                    self._service.move_pos('right')
                    self._render()
                if event.key == pygame.K_1:
                    self._service.insert_number(1)
                    self._render()
                if event.key == pygame.K_2:
                    self._service.insert_number(2)
                    self._render()
                if event.key == pygame.K_3:
                    self._service.insert_number(3)
                    self._render()
                if event.key == pygame.K_4:
                    self._service.insert_number(4)
                    self._render()
                if event.key == pygame.K_5:
                    self._service.insert_number(5)
                    self._render()
                if event.key == pygame.K_6:
                    self._service.insert_number(6)
                    self._render()
                if event.key == pygame.K_7:
                    self._service.insert_number(7)
                    self._render()
                if event.key == pygame.K_8:
                    self._service.insert_number(8)
                    self._render()
                if event.key == pygame.K_9:
                    self._service.insert_number(9)
                    self._render()
                if event.key in (pygame.K_DELETE, pygame.K_BACKSPACE):
                    self._service.insert_number(0)
                    self._render()

    def _render(self):
        self._renderer.render()
