import pygame


class GameLoop:
    """Peliruudukkotilassa pelisilmukkaa kuvaava luokka.
    """

    def __init__(self, service, renderer, event_queue):
        """Attributes: 
            serice : GameService sovelluslogiikasta vastaava luokka
            renderer : kuvan piirtämisestä vastaava luokka Renderer
            event_queue : pygame tapahtumien käsittelyä varten luokka EventQueue
            clock : pygame kello, jolla tahdistetaan kuvan piirtäminen 30 kuvaan sekunnissa.        

        Args:
            service (GameService): Sovelluslogiikasta vastaava luokka GameService.
            renderer (Renderer): Kuvan piirtämisestä vastaava luokka Renderer
            event_queue (EventQueue): Pygame tapahtumien käsittelyä varten luokka EventQueue
        """
        self._service = service
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = pygame.time.Clock()

    def start(self):
        """Metodi, joka aloittaa pelitilan. Silmukassa kutsuu metodia _handle_events, kunnes
        halutaan poistua pelitilasta. Kutsuu _render metodia piirtämistä varten ja tahdistaa
        kellon silmukassa. Poistuessa kutsuu GameService luokan metodia save_game() ja palauttaa
        koko pelistä poitumisen halun muodossa True tai False, jos palataan vain aloitusruudulle.

        Returns:
            Boolean: Palauttaa tiedon, siirrytäänkö aloitusruudulle vai kokonaan pois pelistä.
        """
        self._quit = True
        self._render()
        while True:
            if self._handle_events() is False:
                break
            self._render()
            self._clock.tick(30)

        self._service.save_game()
        return self._quit

    def _handle_events(self):
        """Tapahtumien käsittelystä vastaava metodi.

        Returns:
            Boolan: Palauttaa False metodille start(), kun halutaan poistua pelistä.
        """
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
                if event.key == pygame.K_ESCAPE:
                    self._quit = False
                    return False

    def _render(self):
        self._renderer.render()
