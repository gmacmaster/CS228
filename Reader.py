import numpy as np
import pickle
pickle_in = open("./userData/gesture0.p", "rb")


class READER:
    def __init__(self):
        self.gestureData = pickle.load(pickle_in)
        print(self.gestureData)
