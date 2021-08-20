#497. Random Point in Non-overlapping rectangle:
import numpy as np 
class Solution:
    def __init__(self, rects: List[List[int]]):
    	self.rects = rects
        self.weights = []
        for w in rects:
            self.weights.append((w[2] - w[0] + 1) * (w[3] - w[1] + 1))
        totalWeights = sum(self.weights)
        #Construct a cumulative distribution function.
        self.weights = [t/totalWeights for t in self.weights]

    def pick(self):
        #To randomly choose one rectangle here:
        rectSelected = random.choices(population = self.rects, weights = self.weights, k = 1)[0]
        xSelected = random.randint(rectSelected[0], rectSelected[2])
        ySelected = random.randint(rectSelected[1], rectSelected[3])
        return [xSelected, ySelected]
