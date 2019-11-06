import sys

sys.path.append('../../x64')
sys.path.insert(0, '../..')
import Leap
from pygameWindow import PYGAME_WINDOW
import random
import constants
import pickle
import numpy as np
import time

database = pickle.load(open('userData/database.p', 'rb'))
userName = raw_input('Please enter your name: ')
if userName in database:
    print('welcome back ' + userName + '.')
    database[userName]['logins'] = database[userName]['logins'] + 1
else:
    database[userName] = {}
    database[userName]['logins'] = 1
    database[userName]['0attempted'] = 0
    database[userName]['1attempted'] = 0
    database[userName]['2attempted'] = 0
    database[userName]['3attempted'] = 0
    database[userName]['4attempted'] = 0
    database[userName]['5attempted'] = 0
    database[userName]['6attempted'] = 0
    database[userName]['7attempted'] = 0
    database[userName]['8attempted'] = 0
    database[userName]['9attempted'] = 0
    database[userName]['numTries'] = 0
    print('welcome ' + userName + '.')
userRecord = database[userName]

controller = Leap.Controller()

pygameWindow = PYGAME_WINDOW()

clf = pickle.load(open('../Del6/userData/classifier.p', 'rb'))
testData = np.zeros((1, 30), dtype='f')
k = 0
x = 350
y = 350

xMin = 1000.0
xMax = -1000.0
yMin = 1000.0
yMax = -1000.0

programState = 0
programMode = 0
userHandCentered = False
centeredTimes = 0
minCenteredTimes = 500
centeringComplete = False
numCorrectSigns = 0
currentSignAttempts = 0
maxSignAttempts = 500
signToShow = 1


def CenterData(X):
    allXCoordinates = X[0, ::3]
    meanValue = allXCoordinates.mean()
    X[0, ::3] = allXCoordinates - meanValue
    allYCoordinates = X[0, 1::3]
    meanValue = allYCoordinates.mean()
    X[0, 1::3] = allYCoordinates - meanValue
    allZCoordinates = X[0, 2::3]
    meanValue = allZCoordinates.mean()
    X[0, 2::3] = allZCoordinates - meanValue
    return X


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
    global xMax, xMin, yMax, yMin, programState
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
    devisor = 2
    if (xMax > constants.pygameWindowWidth / devisor):
        xMax = constants.pygameWindowWidth / devisor
    if (yMax > constants.pygameWindowDepth / devisor):
        yMax = constants.pygameWindowDepth / devisor
    x = Scale(x, xMin, xMax, 0, constants.pygameWindowWidth / devisor)
    y = Scale(y, yMin, yMax, 0, constants.pygameWindowDepth / devisor)
    return x, y


def Handle_Bone(bone, width, b):
    global k, testData
    base = Handle_Vector_From_Leap(bone.prev_joint)
    tip = Handle_Vector_From_Leap(bone.next_joint)
    pygameWindow.Draw_Black_Line(base, tip, width)
    if (b == 0) or (b == 3):
        testData[0, k] = bone.next_joint[0]
        testData[0, k + 1] = bone.next_joint[1]
        testData[0, k + 2] = bone.next_joint[2]
        k = k + 3


def Handle_Finger(finger):
    for b in range(4):
        bone = finger.bone(b)
        Handle_Bone(bone, (4 - b), b)


def Handle_Palm_Position(palm):
    global programState, minCenteredTimes, centeredTimes
    leftMost = -150
    rightMost = 150
    maxHeight = 300
    minHeight = 200
    topMost = -100
    bottomMost = 100
    direction = ''
    moveNeeded = False
    if palm[0] < leftMost:
        direction = 'right'
        moveNeeded = True
    elif palm[0] > rightMost:
        direction = 'left'
        moveNeeded = True
    if palm[1] < minHeight:
        direction = 'up'
        moveNeeded = True
    elif palm[1] > maxHeight:
        direction = 'down'
        moveNeeded = True
    if palm[2] < topMost:
        direction = 'forward'
        moveNeeded = True
    elif palm[2] > bottomMost:
        direction = 'back'
        moveNeeded = True
    if (not moveNeeded):
        centeredTimes = centeredTimes + 1
        if centeredTimes >= minCenteredTimes:
            pygameWindow.Load_Image('good.jpg', constants.pygameWindowWidth / 2, 0, True)
            programState = 2
        else:
            pygameWindow.Load_Image('wave.png', constants.pygameWindowWidth / 2, 0, True)
            if centeredTimes % 2 == 0:
                pygameWindow.Draw_Line((constants.pygameWindowWidth / 2, 0),
                                       (constants.pygameWindowWidth / 2, constants.pygameWindowDepth / 2), 4,
                                       (0, 255, 0))
                pygameWindow.Draw_Line((constants.pygameWindowWidth / 2, constants.pygameWindowDepth / 2),
                                       (constants.pygameWindowWidth, constants.pygameWindowDepth / 2), 4, (0, 255, 0))
    else:
        # print(direction)
        pygameWindow.Load_Image(direction + '.png', constants.pygameWindowWidth / 2, 0, True)
        pygameWindow.Draw_Line((constants.pygameWindowWidth / 2, 0),
                               (constants.pygameWindowWidth / 2, constants.pygameWindowDepth / 2), 3, (255, 0, 0))
        pygameWindow.Draw_Line((constants.pygameWindowWidth / 2, constants.pygameWindowDepth / 2),
                               (constants.pygameWindowWidth, constants.pygameWindowDepth / 2), 3, (255, 0, 0))
        programState = 1
        centeredTimes = 0


def Handle_Frame(frame):
    global x, y, xMax, xMin, yMax, yMin, userHandCentered
    hand = frame.hands[0]
    if (not userHandCentered):
        Handle_Palm_Position(hand.palm_position)
    fingers = hand.fingers
    for finger in fingers:
        Handle_Finger(finger)

def Handle_Frame_Circle(frame):
    # May have to switch xMax, yMax etc variable to other name
    global x, y, xMax, xMin, yMax, yMin
    hand = frame.hands[0]
    palm = hand.palm_position
    fingers = hand.fingers
    indexFingerList = fingers.finger_type(1)
    indexFinger = indexFingerList[0]
    distalPhalanx = indexFinger.bone(3)
    tip = distalPhalanx.next_joint
    print tip
    print palm
    x = int(palm[0])
    y = int(palm[1])
    y = constants.pygameWindowDepth - y
    if (x < xMin):
        xMin = x
    if (x > xMax):
        xMax = x
    if (y < yMin):
        yMin = y
    if (y > yMax):
        yMax = y


def DispalyDirections():
    global x, y, xMax, xMin, yMax, yMin
    pickle_in = open("../userDirections/directions0.p", "rb")
    gestureData = pickle.load(pickle_in)
    for x in range(100):
        for i in range(5):
            for j in range(4):
                currentBone = gestureData[i, j, :, x]
                xBaseNotYetScaled = currentBone[0]
                yBaseNotYetScaled = currentBone[2]
                xTipNotYetScaled = currentBone[3]
                yTipNotYetScaled = currentBone[5]
                xBaseScaled = Scale(xBaseNotYetScaled, xMin, xMax, 0, constants.pygameWindowWidth)
                xTipScaled = Scale(xTipNotYetScaled, xMin, xMax, 0, constants.pygameWindowWidth)
                yBaseScaled = Scale(yBaseNotYetScaled, yMin, yMax, 0, constants.pygameWindowDepth)
                yTipScaled = Scale(yTipNotYetScaled, yMin, yMax, 0, constants.pygameWindowDepth)
                pygameWindow.Draw_Black_Line((xBaseScaled, yBaseScaled), (xTipScaled, yTipScaled), 2)

def GetNextSign():
    global userRecord
    least = userRecord['1attempted']
    sign = 1
    leastSuccessful = [1]
    for r in userRecord:
        if r.find('attempted') != -1:
            if userRecord[r] < least:
                least = userRecord[r]
                leastSuccessful = [int(r[0])]
            elif userRecord[r] == least:
                leastSuccessful.append(int(r[0]))
    return leastSuccessful[random.randint(0, len(leastSuccessful)-1)]


signToShow = GetNextSign()
while True:
    global k, programState, numCorrectSigns, currentSignAttempts, signToShow, userRecord, database, maxSignAttempts, database, userName, programMode
    frame = controller.frame()
    pygameWindow.Prepare()
    if programMode == 0:
        pygameWindow.Load_Image('wave.png', 100, 100, False)
        if len(frame.hands) > 0:
            programMode = 1
    elif programMode == 1:
        pygameWindow.Load_Image('wave.png', 100, 100, False)
        Handle_Frame_Circle(frame)
        pygameX = Scale(x, xMin, xMax, 0, constants.pygameWindowWidth)
        pygameY = Scale(y, yMin, yMax, 0, constants.pygameWindowDepth)
        pygameWindow.Draw_Black_Circle(pygameX, pygameY)
        if len(frame.hands) == 0:
            programMode = 0
    elif programMode == 2:
        if programState == 0:
            # pygameWindow.Draw_Black_Line((50, 50), (50, 100), 2)
            pygameWindow.Load_Image('wave.png', 100, 100, False)
            if len(frame.hands) > 0:
                programState = 1
                numCorrectSigns = 0
        elif programState == 1:
            pygameWindow.Display_Tries(userRecord)
            pygameWindow.Display_Leaders(database, userName)
            k = 0
            Handle_Frame(frame)
            if len(frame.hands) == 0:
                programState = 0
        elif programState == 2:
            pygameWindow.Display_Time_Left((maxSignAttempts-currentSignAttempts)/100 + 1)
            pygameWindow.Display_Leaders(database, userName)
            if int(userRecord[str(signToShow) + 'attempted']) < 3:
                maxSignAttempts = 500
                pygameWindow.Display_Current_Sign(signToShow)
            elif int(userRecord[str(signToShow) + 'attempted']) < 5:
                maxSignAttempts = 349
            if int(userRecord[str(signToShow) + 'attempted']) >= 5:
                maxSignAttempts = 250
                pygameWindow.Display_Current_Sign_Large(signToShow)
            else:
                pygameWindow.Load_Image(str(signToShow) + '.jpg', constants.pygameWindowWidth / 2,
                                        constants.pygameWindowDepth / 2, True)
            pygameWindow.Display_Tries(userRecord)
            k = 0
            Handle_Frame(frame)
            testData = CenterData(testData)
            predictedClass = clf.Predict(testData)
            print('predictedClass: ' + str(predictedClass))
            print('sign: ' + str(signToShow))
            print('***')
            currentSignAttempts = currentSignAttempts + 1
            if currentSignAttempts >= maxSignAttempts:
                programState = 4
                pygameWindow.Load_Image('bad.png', constants.pygameWindowWidth / 2, 0, True)
            if predictedClass == signToShow:
                numCorrectSigns = numCorrectSigns + 1
                pygameWindow.Draw_Line((constants.pygameWindowWidth / 2, constants.pygameWindowDepth),
                                       (constants.pygameWindowWidth / 2, constants.pygameWindowDepth / 2), 4, (0, 255, 0))
                pygameWindow.Draw_Line((0, constants.pygameWindowDepth / 2),
                                       (constants.pygameWindowWidth / 2, constants.pygameWindowDepth / 2), 4, (0, 255, 0))
            else:
                pygameWindow.Draw_Line((constants.pygameWindowWidth / 2, constants.pygameWindowDepth),
                                       (constants.pygameWindowWidth / 2, constants.pygameWindowDepth / 2), 4, (255, 0, 0))
                pygameWindow.Draw_Line((0, constants.pygameWindowDepth / 2),
                                       (constants.pygameWindowWidth / 2, constants.pygameWindowDepth / 2), 4, (255, 0, 0))
            if numCorrectSigns >= 150:
                programState = 3
                pygameWindow.Load_Image('done.png', constants.pygameWindowWidth / 2, 0, True)
            if len(frame.hands) == 0:
                programState = 0
                numCorrectSigns = 0
        elif programState == 3:
            print('Success')
            time.sleep(2)
            programState = 1
            numCorrectSigns = 0
            currentSignAttempts = 0
            userRecord[str(signToShow) + 'attempted'] = userRecord[str(signToShow) + 'attempted'] + 1
            userRecord['numTries'] = userRecord['numTries'] + 1
            signToShow = GetNextSign()
            print(userRecord)
            pickle.dump(database, open('userData/database.p', 'wb'))
        elif programState == 4:
            print('Failure')
            userRecord['numTries'] = userRecord['numTries'] + 1
            numCorrectSigns = 0
            currentSignAttempts = 0
            time.sleep(2)
            signToShow = GetNextSign()
            programState = 1
            pickle.dump(database, open('userData/database.p', 'wb'))
        if not programState == 0:
            pygameWindow.Draw_Black_Line((constants.pygameWindowWidth / 2, 0),
                                         (constants.pygameWindowWidth / 2, constants.pygameWindowDepth), 2)
            pygameWindow.Draw_Black_Line((0, constants.pygameWindowDepth / 2),
                                         (constants.pygameWindowWidth, constants.pygameWindowDepth / 2), 2)
    elif programMode == 3:
        pass
    pygameWindow.Reveal()
