import pygame
from service.game_service import game_service, NoSavedGame
from ui.renderer import Renderer
from ui.gameloop import GameLoop


class Menu:
    """Aloitusvalikkoa kuvaava luokka.
    """

    def __init__(self, display, width, eventqueue, game_service=game_service):
        """Attributes:
            display : pygame näyttö
            backround_color : näytön taustaväri
            events : tapahtumien käsittelyluokka EventQueue
            button_color : Valikon painikkeiden väri
            font : fontti, jolla näytön tekstit on kirjoitettu
            width : näytön leveys (näyttö on neliö, eli sama korkeus)
            game_service : sovelluslogiikasta vastaava luokka GameService

        Args:
            display : pygame näyttö
            width (int): näytön leveys ja korkeus
            eventqueue (EventQueue): pygame tapahtumia kuvaava luokka EventQueue
            game_service (GameService, optional): Sovelluslogiikasta vastaava luokka. Oletusarvona sama game_service
            kuin mitä muutkin luokat käyttävät.
        """
        self._display = display
        self._backround_color = (251, 247, 245)
        self._events = eventqueue
        self._button_color = (255, 200, 200)
        self._font = pygame.font.SysFont('Comic Sans MS', 50)
        self._width = width
        self._game_service = game_service

    def initialize(self):
        """Metodi, joka aloittaa aloitusruudukon piirtämisen ja tapahtumien käsittelyn.
        """
        self._render()
        self._menu_loop()

    def _render(self):
        self._display.fill(self._backround_color)
        new_game_button = self._font.render(
            "New Game", True, "black", self._button_color)
        resume_button = self._font.render(
            "Resume Game", True, "black", self._button_color)
        quit_button = self._font.render(
            "Quit", True, "black", self._button_color)
        self._new_game_rect = new_game_button.get_rect()
        self._resume_rect = resume_button.get_rect()
        self._quit_rect = quit_button.get_rect()
        self._new_game_rect.center = (self._width//2, self._width//4)
        self._resume_rect.center = (self._width//2, self._width//4+150)
        self._quit_rect.center = (self._width//2, self._width//4+300)
        self._display.blit(new_game_button, self._new_game_rect)
        self._display.blit(resume_button, self._resume_rect)
        self._display.blit(quit_button, self._quit_rect)
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
                    quit_collide = self._quit_rect.collidepoint(point)
                    if quit_collide:
                        running = False
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
