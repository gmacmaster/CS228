import numpy as np
import pickle

import knnNew

knn = knnNew.KNN()
knn.Use_K_Of(15)


def ReshapeData(set1, set2):
    X = np.zeros((2000, 5 * 4 * 6), dtype='f')
    y = np.zeros(2000, dtype='i')
    for row in range(0, 1000):
        y[row] = 6
        y[row + 1000] = 7
        col = 0
        for finger in range(0, 5):
            for bone in range(0, 2):
                for coordinate in range(0, 3):
                    X[row, col] = set1[finger, bone, coordinate, row]
                    X[row + 1000, col] = set2[finger, bone, coordinate, row]
                    col = col + 1
    return X, y


def ReduceData(X):
    X = np.delete(X, 1, 1)
    X = np.delete(X, 1, 1)

    X = np.delete(X, 0, 2)
    X = np.delete(X, 0, 2)
    X = np.delete(X, 0, 2)
    return X


def CenterData(X):
    allXCoordinates = X[:, :, 0, :]
    meanValue = allXCoordinates.mean()
    X[:, :, 0, :] = allXCoordinates - meanValue
    allYCoordinates = X[:, :, 1, :]
    meanValue = allYCoordinates.mean()
    X[:, :, 1, :] = allYCoordinates - meanValue
    allZCoordinates = X[:, :, 2, :]
    meanValue = allZCoordinates.mean()
    X[:, :, 2, :] = allZCoordinates - meanValue
    return X


pickle_in1 = open("./userData/test6.p", "rb")
pickle_in2 = open("./userData/test7.p", "rb")
pickle_in3 = open("./userData/train6.p", "rb")
pickle_in4 = open("./userData/train7.p", "rb")
test6 = pickle.load(pickle_in1)
test7 = pickle.load(pickle_in2)
train6 = pickle.load(pickle_in3)
train7 = pickle.load(pickle_in4)
test6 = ReduceData(test6)
test7 = ReduceData(test7)
train6 = ReduceData(train6)
train7 = ReduceData(train7)
test6 = CenterData(test6)
test7 = CenterData(test7)
train6 = CenterData(train6)
train7 = CenterData(train7)

trainData = ReshapeData(train6, train7)
trainX = trainData[0]
trainy = trainData[1]
testData = ReshapeData(test6, test7)
testX = testData[0]
testy = testData[1]
knn.Fit(trainX, trainy)

numCorrect = 0
total = 0
for row in range(0, 2000):
    total = total + 1
    prediction = int(knn.Predict(testX[row]))
    actualValue = testy[row]
    if (prediction == actualValue):
        numCorrect = numCorrect + 1
print(numCorrect)
print(str(float(numCorrect / float(total)) * 100.0) + "% Correct")
# print(trainX)
# print(trainX.shape)
# print(trainy)
# print(trainy.shape)
# print(testX)
# print(testX.shape)
# print(testy)
# print(testy.shape)
