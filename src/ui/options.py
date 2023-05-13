import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox


class Options:
    """Options -valikkoa kuvaava luokka
    """

    def __init__(self, display, eventqueue, font):
        """Options -valikkonäkymää kuvaava luokka

        Attr:
            display : pelinäyttö
            events : Pygame tapahtumia kuvaava luokka EventQueue
            backround_color : ruudun taustaväri
            font : Pygame fontti
            slider : Luikuvalikko, jolla voi muuttaa vaikeustasoa
            output : tekstikenttä, joka kertoo liukuvalikon nykyisen arvon
        Args:
            display : pelinäyttö
            eventqueue : Pygame tapahtumat
            font : Pygame fontti 
        """
        self._display = display
        self._events = eventqueue
        self._backround_color = (251, 247, 245)
        self._font = font
        width, height = self._get_screen_size()
        self._slider = Slider(self._display, 100, height//4, 400, 40,
                              min=1, max=150, step=1, colour=(255, 200, 200), initial=20)
        self._output = TextBox(self._display, 275, 200, 50, 50, fontSize=30)
        self._output.disable()

    def _get_screen_size(self):
        return self._display.get_size()

    def _render(self):
        self._display.fill(self._backround_color)
        difficulty_text = self._font.render("Difficulty:", True, "black")
        difficulty_text_rect = difficulty_text.get_rect()
        width, height = self._get_screen_size()
        difficulty_text_rect.center = (width//2, height//8)
        back_text = self._font.render("Back", True, "black", (255, 200, 200))
        self._back_text_rect = back_text.get_rect()
        self._back_text_rect.center = (width//2, height-100)
        self._display.blit(difficulty_text, difficulty_text_rect)
        self._display.blit(back_text, self._back_text_rect)
        self._output.setText(self._slider.getValue())

        pygame_widgets.update(self._events.get())
        pygame.display.update()

    def start(self):
        """Metodi, joka käynnistää options -valikon

        Returns:
            Tuple : Tieto, lopetetaanko koko ohjelma (True/False) ja asetettu vaikeustaso
        """
        self._quit = True
        self._render()
        while True:
            if self._handle_events() is False:
                break
            self._render()

        return self._quit, self._slider.getValue()

    def _handle_events(self):
        for event in self._events.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                point = pygame.mouse.get_pos()
                if self._back_text_rect.collidepoint(point):
                    self._quit = False
                    return False
