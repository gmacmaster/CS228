import numpy as np
import pickle

import knnNew as knn

knn = knn.KNN()
knn.Use_K_Of(15)


def ReshapeData(set1, set2, set3):
    X = np.zeros((3000, 5 * 6), dtype='f')
    y = np.zeros(3000, dtype='i')
    for row in range(0, 1000):
        y[row] = 6
        y[row + 1000] = 7
        y[row + 2000] = 1
        col = 0
        for finger in range(0, 5):
            for bone in range(0, 2):
                for coordinate in range(0, 3):
                    X[row, col] = set1[finger, bone, coordinate, row]
                    X[row + 1000, col] = set2[finger, bone, coordinate, row]
                    X[row + 2000, col] = set3[finger, bone, coordinate, row]
                    col = col + 1
    return X, y


def ReshapeDataSets(sets, values):
    X = np.zeros((len(values) * 1000, 5 * 6), dtype='f')
    y = np.zeros(len(values) * 1000, dtype='i')
    for row in range(0, 1000):
        for valNum in range(len(values)):
            y[row + (valNum * 1000)] = values[valNum]
        col = 0
        for finger in range(0, 5):
            for bone in range(0, 2):
                for coordinate in range(0, 3):
                    for setNum in range(len(sets)):
                        X[row + (setNum * 1000), col] = sets[setNum][finger, bone, coordinate, row]
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


def ReduceAndCenter(data):
    return CenterData(ReduceData(data))


test1 = ReduceAndCenter(pickle.load(open("./userData/Lin_test1.p", "rb")))
train1 = ReduceAndCenter(pickle.load(open("./userData/Lin_train1.p", "rb")))
test1_1 = ReduceAndCenter(pickle.load(open("./userData/Newton_test1.p", "rb")))
train1_1 = ReduceAndCenter(pickle.load(open("./userData/Newton_train1.p", "rb")))
test2 = ReduceAndCenter(pickle.load(open("./userData/Liu_test2.p", "rb")))
train2 = ReduceAndCenter(pickle.load(open("./userData/Liu_train2.p", "rb")))
test2_1 = ReduceAndCenter(pickle.load(open("./userData/Apple_test2.p", "rb")))
train2_1 = ReduceAndCenter(pickle.load(open("./userData/Apple_train2.p", "rb")))
train3 = ReduceAndCenter(pickle.load(open("./userData/Liu_train3.p", "rb")))
test3 = ReduceAndCenter(pickle.load(open("./userData/Liu_test3.p", "rb")))
train3_1 = ReduceAndCenter(pickle.load(open("./userData/train3_1.p", "rb")))
test3_1 = ReduceAndCenter(pickle.load(open("./userData/test3_1.p", "rb")))
train4 = ReduceAndCenter(pickle.load(open("./userData/Ortigara_train4.p", "rb")))
test4 = ReduceAndCenter(pickle.load(open("./userData/Ortigara_test4.p", "rb")))
train4_1 = ReduceAndCenter(pickle.load(open("./userData/Deluca_train4.p", "rb")))
test4_1 = ReduceAndCenter(pickle.load(open("./userData/Deluca_test4.p", "rb")))
train5 = ReduceAndCenter(pickle.load(open("./userData/Ortigara_train5.p", "rb")))
test5 = ReduceAndCenter(pickle.load(open("./userData/Ortigara_test5.p", "rb")))
train5_1 = ReduceAndCenter(pickle.load(open("./userData/Warren_train5.p", "rb")))
test5_1 = ReduceAndCenter(pickle.load(open("./userData/Warren_test5.p", "rb")))
test6 = ReduceAndCenter(pickle.load(open("./userData/test6.p", "rb")))
train6 = ReduceAndCenter(pickle.load(open("./userData/train6.p", "rb")))
test6_1 = ReduceAndCenter(pickle.load(open("./userData/Peck_test6.p", "rb")))
train6_1 = ReduceAndCenter(pickle.load(open("./userData/Peck_train6.p", "rb")))
test7 = ReduceAndCenter(pickle.load(open("./userData/test7.p", "rb")))
train7 = ReduceAndCenter(pickle.load(open("./userData/train7.p", "rb")))
test7_1 = ReduceAndCenter(pickle.load(open("./userData/Rubin_test7.p", "rb")))
train7_1 = ReduceAndCenter(pickle.load(open("./userData/Rubin_train7.p", "rb")))
test8 = ReduceAndCenter(pickle.load(open("./userData/Rubin_test8.p", "rb"))) #Lefty
train8 = ReduceAndCenter(pickle.load(open("./userData/Rubin_train8.p", "rb"))) #Lefty
test8_1 = ReduceAndCenter(pickle.load(open("./userData/Erickson_test8.p", "rb")))
train8_1 = ReduceAndCenter(pickle.load(open("./userData/Erickson_train8.p", "rb")))
test9 = ReduceAndCenter(pickle.load(open("./userData/Saulean_test9.p", "rb")))
train9 = ReduceAndCenter(pickle.load(open("./userData/Saulean_train9.p", "rb")))
test9_1 = ReduceAndCenter(pickle.load(open("./userData/Zonay_test9.p", "rb")))
train9_1 = ReduceAndCenter(pickle.load(open("./userData/Zonay_train9.p", "rb")))
test0 = ReduceAndCenter(pickle.load(open("./userData/Lin_test0.p", "rb")))
train0 = ReduceAndCenter(pickle.load(open("./userData/Lin_train0.p", "rb")))
test01 = ReduceAndCenter(pickle.load(open("./userData/Childs_test0.p", "rb")))
train01 = ReduceAndCenter(pickle.load(open("./userData/Childs_train0.p", "rb")))

# trainData = ReshapeData(train6, train7, train1)
trainData = ReshapeDataSets(
    [train1_1, train2_1, train3_1, train4, train5, train6, train7, train8_1, train9, train01],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
trainX = trainData[0]
trainy = trainData[1]
testData = ReshapeDataSets(
    [test1_1, test2_1, test3_1, train4, test5, test6, test7, test8_1, test9, test01],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
testX = testData[0]
testy = testData[1]
knn.Fit(trainX, trainy)

numCorrect = 0
total = 0
for row in range(0, len(testData[0])):
    total = total + 1
    prediction = int(knn.Predict(testX[row]))
    actualValue = testy[row]
    if (prediction == actualValue):
        numCorrect = numCorrect + 1
print(numCorrect)
print(str(float(numCorrect / float(total)) * 100.0) + "% Correct")
pickle.dump(knn, open('userData/classifier.p', 'wb'))
# print(trainX)
# print(trainX.shape)
# print(trainy)
# print(trainy.shape)
# print(testX)
# print(testX.shape)
# print(testy)
# print(testy.shape)
