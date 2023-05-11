import pygame
from ui.menu import Menu
from ui.eventqueue import EventQueue


def main():
    width = 550
    display = pygame.display.set_mode((width, width))
    pygame.display.set_caption("Sudoku")
    pygame.init()
    event_queue = EventQueue()
    menu = Menu(display, event_queue)
    menu.initialize()
    pygame.quit()


if __name__ == "__main__":
    main()
