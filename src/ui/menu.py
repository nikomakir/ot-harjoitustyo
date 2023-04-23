import pygame
from service.grid import GameGrid
from ui.renderer import Renderer
from ui.gameloop import GameLoop


class Menu:
    def __init__(self, display, width, eventqueue):
        self._display = display
        self._backround_color = (251, 247, 245)
        self._events = eventqueue
        self._button_color = (255, 200, 200)
        self._font = pygame.font.SysFont('Comic Sans MS', 50)
        self._width = width

    def initialize(self):
        self._render()
        self._menu_loop()

    def _render(self):
        self._display.fill(self._backround_color)
        pygame.display.update()
        new_game_button = self._font.render(
            "New Game", True, "black", self._button_color)
        resume_button = self._font.render(
            "Resume Game", True, "gray", self._button_color)
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
                        game_grid = GameGrid()
                        renderer = Renderer(self._display, game_grid)
                        game_loop = GameLoop(game_grid, renderer, self._events)
                        game_loop.start()
                        running = False
                    elif resume_button_collide:
                        pass
