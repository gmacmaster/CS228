import sys

sys.path.append('../x64')
sys.path.insert(0, '..')
import Leap
from pygameWindow import PYGAME_WINDOW
import random
import constants

controller = Leap.Controller()

pygameWindow = PYGAME_WINDOW()

x = 350
y = 350

xMin = 1000.0
xMax = -1000.0
yMin = 1000.0
yMax = -1000.0


def Perturb_Circle_Position():
    global x, y
    fourSidedDieRoll = random.randint(1, 4)
    if fourSidedDieRoll == 1:
        x = x - constants.circleVelocity
    elif fourSidedDieRoll == 2:
        x = x + constants.circleVelocity
    elif fourSidedDieRoll == 3:
        y = y - constants.circleVelocity
    else:
        y = y + constants.circleVelocity


def Scale(num, l1, h1, l2, h2):
    scaledNum = num
    rangeOne = h1 - l1
    rangeTwo = h2 - l2
    if rangeOne == 0:
        return scaledNum
    else:
        scaledNum = (((num - l1) * rangeTwo) / rangeOne) + l2
        return int(scaledNum)


def Draw_Black_Line(xBase, yBase, xTip, yTip):
    print(xBase, yBase, xTip, yTip)


def Handle_Vector_From_Leap(v):
    global xMax, xMin, yMax, yMin
    x = v[0]
    y = v[2]
    if (x < xMin):
        xMin = x
    if (x > xMax):
        xMax = x
    if (y < yMin):
        yMin = y
    if (y > yMax):
        yMax = y
    x = Scale(x, xMin, xMax, 0, constants.pygameWindowWidth)
    y = Scale(y, yMin, yMax, 0, constants.pygameWindowDepth)
    return x, y


def Handle_Bone(bone, width):
    base = Handle_Vector_From_Leap(bone.prev_joint)
    tip = Handle_Vector_From_Leap(bone.next_joint)
    pygameWindow.Draw_Black_Line(base, tip, 1)


def Handle_Finger(finger):
    for b in range(4):
        bone = finger.bone(b)
        Handle_Bone(bone, (4-b))


def Handle_Frame(frame):
    global x, y, xMax, xMin, yMax, yMin
    hand = frame.hands[0]
    fingers = hand.fingers
    for finger in fingers:
        Handle_Finger(finger)
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


while True:
    frame = controller.frame()
    pygameWindow.Prepare()
    if len(frame.hands) > 0:
        Handle_Frame(frame)
    pygameX = Scale(x, xMin, xMax, 0, constants.pygameWindowWidth)
    pygameY = Scale(y, yMin, yMax, 0, constants.pygameWindowDepth)
    # pygameWindow.Draw_Black_Circle(pygameX, pygameY)
    pygameWindow.Reveal()
