import pygame
import constants

white = (255, 255, 255)


class PYGAME_WINDOW:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.signFont = pygame.font.SysFont('timesnewroman', 80)
        self.headerFont = pygame.font.SysFont('timesnewroman', 18)
        self.textFont = pygame.font.SysFont('timesnewroman', 16)
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

    def Draw_Black_Line(self, start_pos, end_pos, width):
        pygame.draw.line(self.screen, (0, 0, 0), start_pos, end_pos, width)

    def Draw_Line(self, start_pos, end_pos, width, color):
        pygame.draw.line(self.screen, color, start_pos, end_pos, width)

    def Load_Image(self, path, x, y, resize):
        image = pygame.image.load(path)
        if resize:
            image = pygame.transform.scale(image, (constants.pygameWindowWidth / 2, constants.pygameWindowDepth / 2))
        self.screen.blit(image, (x, y))

    def Display_Tries(self, userdata):
        self.screen.blit(self.headerFont.render('Sign: Correct Attempts', False, (0, 0, 0)),
                         (10, constants.pygameWindowDepth / 2))
        self.screen.blit(self.textFont.render('0: ' + str(userdata['0attempted']), False, (0, 20, 0)),
                         (10, constants.pygameWindowDepth / 2 + 20))
        self.screen.blit(self.textFont.render('1: ' + str(userdata['1attempted']), False, (0, 20, 0)),
                         (10, constants.pygameWindowDepth / 2 + 35))
        self.screen.blit(self.textFont.render('2: ' + str(userdata['2attempted']), False, (0, 20, 0)),
                         (10, constants.pygameWindowDepth / 2 + 50))
        self.screen.blit(self.textFont.render('3: ' + str(userdata['3attempted']), False, (0, 20, 0)),
                         (10, constants.pygameWindowDepth / 2 + 65))
        self.screen.blit(self.textFont.render('4: ' + str(userdata['4attempted']), False, (0, 20, 0)),
                         (10, constants.pygameWindowDepth / 2 + 80))
        self.screen.blit(self.textFont.render('5: ' + str(userdata['5attempted']), False, (0, 20, 0)),
                         (10, constants.pygameWindowDepth / 2 + 95))
        self.screen.blit(self.textFont.render('6: ' + str(userdata['6attempted']), False, (0, 20, 0)),
                         (10, constants.pygameWindowDepth / 2 + 110))
        self.screen.blit(self.textFont.render('7: ' + str(userdata['7attempted']), False, (0, 20, 0)),
                         (10, constants.pygameWindowDepth / 2 + 125))
        self.screen.blit(self.textFont.render('8: ' + str(userdata['8attempted']), False, (0, 20, 0)),
                         (10, constants.pygameWindowDepth / 2 + 140))
        self.screen.blit(self.textFont.render('9: ' + str(userdata['9attempted']), False, (0, 20, 0)),
                         (10, constants.pygameWindowDepth / 2 + 155))

    def Display_Current_Sign(self, sign):
        self.screen.blit(self.headerFont.render('Current Sign: ' + str(sign), False, (0, 0, 0)),
                         (10, constants.pygameWindowDepth / 2 + 190))

    def Display_Current_Sign_Large(self, sign):
        self.screen.blit(self.signFont.render('Sign: ' + str(sign), True, (0, 0, 0)),
                         (constants.pygameWindowWidth / 2 + 10, constants.pygameWindowDepth / 2 + 120))


    def Display_Time_Left(self, time):
        self.screen.blit(self.headerFont.render('Time Left: ' + str(time), False, (0, 0, 0)),
                         (10, constants.pygameWindowDepth / 2 + 170))
