from pygameWindow import PYGAME_WINDOW
import random
import constants

pygameWindow = PYGAME_WINDOW()

X = 350
Y = 350


def Perturb_Circle_Position():
    global X, Y
    fourSidedDieRoll = random.randint(1, 4)
    if fourSidedDieRoll == 1:
        X = X - constants.circleVelocity
    elif fourSidedDieRoll == 2:
        X = X + constants.circleVelocity
    elif fourSidedDieRoll == 3:
        Y = Y - constants.circleVelocity
    else:
        Y = Y + constants.circleVelocity

while True:
    Perturb_Circle_Position()
    pygameWindow.Prepare()
    pygameWindow.Draw_Black_Circle(X, Y)
    pygameWindow.Reveal()
