import pygame


class Renderer:
    def __init__(self, display, game_service):
        """Peliruudukon piirtämisestä vastaava luokka.
        Attributes:
            display : pygame näyttö
            game_service : sovelluslogiikasta vastaava luokka GameService
            background_color : näytön taustaväri
            font : fontti, jolla numerot piirretään
            original_grid_color : väri, jolla alussa valmiina olevat numerot piirretään
            number_color :  väri, jolla itse syötettävät numerot piirretään
            coice_color : väri, jolla valittu ruutu piirretään

        Args:
            display : pygame näyttö
            game_service (GameService): Sovelluslogiikasta vastaava luokka GameService.
        """
        self._display = display
        self._game_service = game_service
        self._background_color = (251, 247, 245)
        self._font = pygame.font.SysFont('Comic Sans MS', 35)
        self._original_grid_color = (0, 0, 0)
        self._number_color = (52, 31, 151)
        self._choice_color = (255, 200, 200)

    def render(self):
        self._display.fill(self._background_color)
        back_text = self._font.render("Esc = Back", True, "red")
        back_text_rect = back_text.get_rect()
        back_text_rect.center = (550//2, 20)
        self._display.blit(back_text, back_text_rect)
        x, y = self._game_service.get_pos()
        pygame.draw.rect(self._display, self._choice_color,
                         pygame.Rect(x*50+50, y*50+50, 50, 50))

        for line in range(10):
            if line % 3 == 0:
                pygame.draw.line(self._display, (0, 0, 0),
                                 (50+50*line, 50), (50+50*line, 500), 5)
                pygame.draw.line(self._display, (0, 0, 0),
                                 (50, 50+50*line), (500, 50+50*line), 5)
            pygame.draw.line(self._display, (0, 0, 0),
                             (50+50*line, 50), (50+50*line, 500), 2)
            pygame.draw.line(self._display, (0, 0, 0),
                             (50, 50+50*line), (500, 50+50*line), 2)

        for row in range(9):
            for column in range(9):
                if 0 < self._game_service._grid.start[row][column]:
                    value = self._font.render(
                        str(self._game_service._grid.start[row][column]), True, self._original_grid_color)
                    self._display.blit(value, ((column+1)*50+15, (row+1)*50))
                if self._game_service._grid.grid[row][column] != self._game_service._grid.start[row][column]:
                    value = self._font.render(
                        str(self._game_service._grid.grid[row][column]), True, self._number_color)
                    self._display.blit(value, ((column+1)*50+15, (row+1)*50))
        pygame.display.update()
