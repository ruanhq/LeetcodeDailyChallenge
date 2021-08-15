#398. Random Pick Index:
import random
#randomly ouptut the index of a given target number,
#you can assume that the given target number must exist in 
#the array.


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
            if random.randint(1, count) == countTarget:
                result = i 
        return result