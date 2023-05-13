import pygame
from service.game_service import game_service, NoSavedGame
from ui.renderer import Renderer
from ui.gameloop import GameLoop
from ui.options import Options


class Menu:
    """Aloitusvalikkoa kuvaava luokka.
    """

    def __init__(self, display, eventqueue, game_service=game_service):
        """Attributes:
            display : pygame näyttö
            backround_color : näytön taustaväri
            events : tapahtumien käsittelyluokka EventQueue
            button_color : Valikon painikkeiden väri
            font : fontti, jolla näytön tekstit on kirjoitettu
            game_service : sovelluslogiikasta vastaava luokka GameService

        Args:
            display : pygame näyttö
            eventqueue (EventQueue): pygame tapahtumia kuvaava luokka EventQueue
            game_service (GameService, optional): Sovelluslogiikasta vastaava luokka. Oletusarvona sama game_service
            kuin mitä muutkin luokat käyttävät.
        """
        self._display = display
        self._backround_color = (251, 247, 245)
        self._events = eventqueue
        self._button_color = (255, 200, 200)
        self._font = pygame.font.SysFont('Comic Sans MS', 50)
        self._game_service = game_service
        self._options_menu = Options(self._display, self._events, self._font)

    def initialize(self):
        """Metodi, joka aloittaa aloitusruudukon piirtämisen ja tapahtumien käsittelyn.
        """
        self._render()
        self._menu_loop()

    def _get_screen_size(self):
        return self._display.get_size()

    def _render(self):
        self._display.fill(self._backround_color)
        new_game_button = self._font.render(
            "New Game", True, "black", self._button_color)
        resume_button = self._font.render(
            "Resume Game", True, "black", self._button_color)
        options_button = self._font.render(
            "Options", True, "black", self._button_color)
        self._new_game_rect = new_game_button.get_rect()
        self._resume_rect = resume_button.get_rect()
        self._options_rect = options_button.get_rect()
        width, height = self._get_screen_size()
        self._new_game_rect.center = (width//2, height//4)
        self._resume_rect.center = (width//2, height//2)
        self._options_rect.center = (width//2, int(height*(3/4)))
        self._display.blit(new_game_button, self._new_game_rect)
        self._display.blit(resume_button, self._resume_rect)
        self._display.blit(options_button, self._options_rect)
        pygame.display.update()

    def _menu_loop(self):
        running = True
        while running:
            for event in self._events.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    point = pygame.mouse.get_pos()
                    new_game_collide = self._new_game_rect.collidepoint(point)
                    resume_button_collide = self._resume_rect.collidepoint(
                        point)
                    options_collide = self._options_rect.collidepoint(point)
                    if options_collide:
                        to_quit, difficulty = self._options_menu.start()
                        self._game_service.save_difficulty(difficulty)
                        if to_quit:
                            running = False
                        else:
                            self._render()
                    elif new_game_collide:
                        self._game_service.start_new_game()
                        renderer = Renderer(self._display, self._game_service)
                        game_loop = GameLoop(
                            self._game_service, renderer, self._events)
                        if game_loop.start():
                            running = False
                        else:
                            self._render()
                    elif resume_button_collide:
                        try:
                            self._game_service.load_game()
                        except NoSavedGame:
                            continue
                        renderer = Renderer(self._display, self._game_service)
                        game_loop = GameLoop(
                            self._game_service, renderer, self._events)
                        if game_loop.start():
                            running = False
                        else:
                            self._render()
