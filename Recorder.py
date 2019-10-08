import sys
import random
import constants
import numpy as np
import pickle
import os
import shutil

sys.path.append('../x64')
sys.path.insert(0, '..')
import Leap
from pygameWindow_Del03 import PYGAME_WINDOW

controller = Leap.Controller()

pygameWindow = PYGAME_WINDOW()


class DELIVERABLE:
    def __init__(self):
        self.x = 350
        self.y = 350
        self.xMin = 1000.0
        self.xMax = -1000.0
        self.yMin = 1000.0
        self.yMax = -1000.0
        self.numberOfGestures = 1000
        self.gestureIndex = 0
        self.previousNumberOfHands = 0
        self.currentNumberOfHands = 0
        self.gestureData = np.zeros((5, 4, 6, self.numberOfGestures), dtype='f')
        self.numGestures = 0
        shutil.rmtree('./userDirections')
        os.mkdir('./userDirections')

    def Save_Gesture(self):
        pickle_out = open("./userDirections/directions" + str(self.numGestures) + ".p", "wb")
        self.numGestures = self.numGestures + 1
        pickle.dump(self.gestureData, pickle_out)
        pickle_out.close()

    def Recording_Is_Ending(self):
        if self.currentNumberOfHands == 1 and self.previousNumberOfHands == 2:
            return True
        return False

    def Perturb_Circle_Position(self):
        fourSidedDieRoll = random.randint(1, 4)
        if fourSidedDieRoll == 1:
            self.x = self.x - constants.circleVelocity
        elif fourSidedDieRoll == 2:
            self.x = self.x + constants.circleVelocity
        elif fourSidedDieRoll == 3:
            self.y = self.y - constants.circleVelocity
        else:
            self.y = self.y + constants.circleVelocity

    def Scale(self, num, l1, h1, l2, h2):
        scaledNum = num
        rangeOne = h1 - l1
        rangeTwo = h2 - l2
        if rangeOne == 0:
            return scaledNum
        else:
            scaledNum = (((num - l1) * rangeTwo) / rangeOne) + l2
            return int(scaledNum)

    def Draw_Line(self, xBase, yBase, xTip, yTip):
        print(xBase, yBase, xTip, yTip)

    def Handle_Vector_From_Leap(self, v):
        x = v[0]
        y = v[2]
        if x < self.xMin:
            self.xMin = x
        if x > self.xMax:
            self.xMax = x
        if y < self.yMin:
            self.yMin = y
        if y > self.yMax:
            self.yMax = y
        x = self.Scale(x, self.xMin, self.xMax, 0, constants.pygameWindowWidth)
        y = self.Scale(y, self.yMin, self.yMax, 0, constants.pygameWindowDepth)
        return x, y

    def Handle_Bone(self, bone, b, fingerType):
        base = self.Handle_Vector_From_Leap(bone.prev_joint)
        tip = self.Handle_Vector_From_Leap(bone.next_joint)
        if self.currentNumberOfHands > 1:
            color = (255, 0, 0)
        else:
            color = (0, 255, 0)
        pygameWindow.Draw_Line(base, tip, (4 - b), color)
        if self.currentNumberOfHands == 2:
            self.gestureData[fingerType, b, 0, self.gestureIndex] = bone.prev_joint[0]
            self.gestureData[fingerType, b, 1, self.gestureIndex] = bone.prev_joint[1]
            self.gestureData[fingerType, b, 2, self.gestureIndex] = bone.prev_joint[2]
            self.gestureData[fingerType, b, 3, self.gestureIndex] = bone.next_joint[0]
            self.gestureData[fingerType, b, 4, self.gestureIndex] = bone.next_joint[1]
            self.gestureData[fingerType, b, 5, self.gestureIndex] = bone.next_joint[2]

    def Handle_Finger(self, finger):
        for b in range(4):
            bone = finger.bone(b)
            self.Handle_Bone(bone, b, finger.type)

    def Handle_Frame(self, frame):
        hand = frame.hands[0]
        fingers = hand.fingers
        for finger in fingers:
            self.Handle_Finger(finger)
        if self.currentNumberOfHands == 2:
            print('gesture ' + str(self.gestureIndex) + ' stored.')
            self.gestureIndex = self.gestureIndex + 1
            if self.gestureIndex == self.numberOfGestures:
                self.Save_Gesture()
                exit(0)
        # indexFingerList = fingers.finger_type(1)
        # indexFinger = indexFingerList[0]
        # distalPhalanx = indexFinger.bone(3)
        # tip = distalPhalanx.next_joint
        # x = int(tip[0])
        # y = int(tip[1])
        # y = constants.pygameWindowDepth - y
        # if (x < xMin):
        #     xMin = x
        # if (x > xMax):
        #     xMax = x
        # if (y < yMin):
        #     yMin = y
        # if (y > yMax):
        #     yMax = y
        pass

    def Run_Once(self):
        frame = controller.frame()
        pygameWindow.Prepare()
        self.currentNumberOfHands = len(frame.hands)
        if len(frame.hands) > 0:
            self.Handle_Frame(frame)
        pygameX = self.Scale(self.x, self.xMin, self.xMax, 0, constants.pygameWindowWidth)
        pygameY = self.Scale(self.y, self.yMin, self.yMax, 0, constants.pygameWindowDepth)
        # pygameWindow.Draw_Black_Circle(pygameX, pygameY)
        pygameWindow.Reveal()
        self.previousNumberOfHands = self.currentNumberOfHands
