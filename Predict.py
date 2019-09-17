import matplotlib.pyplot as plt
import numpy as np

import knn

knn = knn.KNN()
knn.Load_Dataset('iris.csv')
# print(knn.data[:, :])
# print(knn.target)
trainX = knn.data[::2, 1:3]
trainy = knn.target[::2]
testX = knn.data[1::2, 1:3]
testy = knn.target[1::2]
knn.Use_K_Of(15)
knn.Fit(trainX, trainy)
x = trainX[:, 0]
y = trainX[:, 1]
xTest = testX[:, 0]
yTest = testX[:, 1]
colors = np.zeros((3, 3), dtype='f')
colors[0, :] = [1, 0.5, 0.5]
colors[1, :] = [0.5, 1, 0.5]
colors[2, :] = [0.5, 0.5, 1]
plt.figure()
[numItems, numFeatures] = knn.data.shape
for i in range(0, numItems / 2):
    itemClass = int(trainy[i])
    currColor = colors[itemClass, :]
    plt.scatter(trainX[i, 0], trainX[i, 1], facecolor=currColor, s=50, lw=2, edgecolor=[0,0,0])
numCorrect = 0
for i in range(0, numItems / 2):
    itemClass = int(testy[i])
    currColor = colors[itemClass, :]
    prediction = int(knn.Predict(testX[i, :]))
    if itemClass == prediction:
        numCorrect = numCorrect + 1
    edgeColor = colors[prediction, :]
    plt.scatter(testX[i, 0], testX[i, 1], facecolor=currColor, s=50, lw=2, edgecolor=edgeColor)
print(numCorrect)
print(str((float(numCorrect)/float(numItems/2))*100.0) + '%')
# plt.scatter(x, y, c=trainy)
# plt.scatter(xTest, yTest, c=trainy)
plt.show()
