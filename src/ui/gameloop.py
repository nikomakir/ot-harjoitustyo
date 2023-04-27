import pygame


class GameLoop:
    def __init__(self, service, renderer, event_queue):
        self._service = service
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = pygame.time.Clock()

    def start(self):
        self._render()
        while True:
            if self._hande_events() is False:
                break
            self._render()
            self._clock.tick(30)

        self._service.save_game()

    def _hande_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._service.move_pos('left')
                if event.key == pygame.K_UP:
                    self._service.move_pos('up')
                if event.key == pygame.K_DOWN:
                    self._service.move_pos('down')
                if event.key == pygame.K_RIGHT:
                    self._service.move_pos('right')
                if event.key == pygame.K_1:
                    self._service.insert_number(1)
                if event.key == pygame.K_2:
                    self._service.insert_number(2)
                if event.key == pygame.K_3:
                    self._service.insert_number(3)
                if event.key == pygame.K_4:
                    self._service.insert_number(4)
                if event.key == pygame.K_5:
                    self._service.insert_number(5)
                if event.key == pygame.K_6:
                    self._service.insert_number(6)
                if event.key == pygame.K_7:
                    self._service.insert_number(7)
                if event.key == pygame.K_8:
                    self._service.insert_number(8)
                if event.key == pygame.K_9:
                    self._service.insert_number(9)
                if event.key in (pygame.K_DELETE, pygame.K_BACKSPACE):
                    self._service.insert_number(0)

    def _render(self):
        self._renderer.render()
