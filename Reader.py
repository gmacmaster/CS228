import numpy as np
import pickle
import os
import constants
import time

from pygameWindow_Del03 import PYGAME_WINDOW


class READER:
    def __init__(self):
        self.pygameWindow = PYGAME_WINDOW()
        self.Get_Dir_Info()
        self.xMin = constants.xMin
        self.xMax = constants.xMax
        self.yMin = constants.yMin
        self.yMax = constants.yMax

    def Scale(self, num, l1, h1, l2, h2):
        scaledNum = num
        rangeOne = h1 - l1
        rangeTwo = h2 - l2
        if rangeOne == 0:
            return scaledNum
        else:
            scaledNum = (((num - l1) * rangeTwo) / rangeOne) + l2
            return int(scaledNum)

    def Get_Dir_Info(self):
        path, dirs, files = next(os.walk('./userData'))
        self.numGestures = len(files)

    def Print_Gestures(self):
        for g in range(self.numGestures - 1):
            pickle_in = open("./userData/gesture" + str(g) + ".p", "rb")
            print(pickle.load(pickle_in))

    def Draw_Gesture(self, g):
        pickle_in = open("./userData/gesture" + str(g) + ".p", "rb")
        gestureData = pickle.load(pickle_in)
        self.pygameWindow.Prepare()
        for i in range(5):
            for j in range(4):
                currentBone = gestureData[i, j, :]
                xBaseNotYetScaled = currentBone[0]
                yBaseNotYetScaled = currentBone[2]
                xTipNotYetScaled = currentBone[3]
                yTipNotYetScaled = currentBone[5]
                xBaseScaled = self.Scale(xBaseNotYetScaled, self.xMin, self.xMax, 0, constants.pygameWindowWidth)
                xTipScaled = self.Scale(xTipNotYetScaled, self.xMin, self.xMax, 0, constants.pygameWindowWidth)
                yBaseScaled = self.Scale(yBaseNotYetScaled, self.yMin, self.yMax, 0, constants.pygameWindowDepth)
                yTipScaled = self.Scale(yTipNotYetScaled, self.yMin, self.yMax, 0, constants.pygameWindowDepth)
                self.pygameWindow.Draw_Line((xBaseScaled, yBaseScaled), (xTipScaled, yTipScaled), 2, (0, 0, 255))
        self.pygameWindow.Reveal()
        time.sleep(0.25)

    def Draw_Each_Gesture_Once(self):
        for g in range(self.numGestures):
            self.Draw_Gesture(g)

    def Draw_Gestures(self):
        while True:
            self.Draw_Each_Gesture_Once()
