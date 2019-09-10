import pygame
import constants

white = (255, 255, 255)


class PYGAME_WINDOW:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((constants.pygameWindowWidth, constants.pygameWindowDepth))

    def Prepare(self):
        pygame.event.get()
        self.screen.fill((255, 255, 255))
        pass

    def Reveal(self):
        pygame.display.update()
        pass

    def Draw_Black_Circle(self, x, y):
        pygame.draw.circle(self.screen, (0, 0, 0), (x, y), 20, 20)

    def Draw_Line(self, start_pos, end_pos, width, color):
        pygame.draw.line(self.screen, color, start_pos, end_pos, width)
