#398. Random Pick Index:
import random
#randomly ouptut the index of a given target number,
#you can assume that the given target number must exist in 
#the array.

#It likes the reservoir sampling where each time 
#using a 1/#currentNumber probability

class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
    def pick(self, target):
        nNumber = len(self.nums)
        result = None
        count = 0
        for i, x in enumerate(self.nums):
            if x == target:
                countTarget += 1
                #like reservoir sampling:
                #each time sample with 1/currentNumber probability here
                #if K distinct values:
                #P(t) = (1/t) * (t/(t+1)) * ..(k-1/k) = 1/k
                if random.randint(1, count) == countTarget:
                    result = i 
        return result

    #Another quicker method, just do one random choice here.
    def pick(self, target):
        targetResult = []
        for i, x in enumerate(self.nums):
            if x == target:
                targetResult.append(i)
        output = random.choice(targetResult)
        return output