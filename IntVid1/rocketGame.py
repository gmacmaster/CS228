import constants
import random
import math


class Asteroid:
    xPos = 0
    yPos = 0
    sign = 0
    hit = False

    def __init__(self):
        self.yPos = -100 - random.randint(1, constants.pygameWindowDepth)
        self.xPos = random.randint(1, constants.pygameWindowWidth)
        self.sign = random.randint(0, 9)
        pass

    def moveX(self, amount):
        self.xPos = self.xPos + amount

    def moveY(self, amount):
        if(self.yPos > constants.pygameWindowDepth):
            self.yPos = -50
            self.xPos = random.randint(1, constants.pygameWindowWidth)
            self.sign = random.randint(0, 9)
        else:
            self.yPos = self.yPos + amount

    def resetLocation(self):
        self.yPos = -50
        self.xPos = random.randint(1, constants.pygameWindowWidth)
        self.sign = random.randint(0, 9)


class RocketGame:
    rocketX = 0
    rocketY = 0

    def __init__(self, xPos, yPos, pygameWindow):
        self.pygameWindow = pygameWindow
        self.rocketX = xPos
        self.rocketY = yPos
        self.health = 0
        self.asteroids = []
        self.level = 0

    def setPos(self, xPos, yPos):
        self.rocketX = xPos
        self.rocketY = yPos

    def checkHit(self, asteroid):
        return math.sqrt((self.rocketX - asteroid.xPos)**2 + (self.rocketY - asteroid.yPos)**2) < 25

    def incrementLevel(self):
        self.level = self.level + 1
        while len(self.asteroids) < self.level * 5:
            newAsteroid = Asteroid()
            self.asteroids.append(newAsteroid)

    def getHealth(self):
        return self.health

    def getLevel(self):
        return self.level

    def reset(self):
        self.health = 100
        self.level = 0
        self.asteroids = []

    def play(self):
        self.pygameWindow.Display_Level(self.level, self.health)
        if len(self.asteroids) == 0:
            self.incrementLevel()
        for asteroid in self.asteroids:
            asteroid.moveY(self.level)
            self.pygameWindow.Display_Asteroid('asteroid.png', asteroid.xPos, asteroid.yPos, 50, 50, asteroid.sign)
            if self.checkHit(asteroid):
                self.health = self.health - 10
                asteroid.resetLocation()