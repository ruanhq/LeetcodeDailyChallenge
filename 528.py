#528. Random Pick with Weight:


class Solution:
    def __init__(self, w: List[int]):
        self.cumulativeSum = []
        cumSum = 0
        for weight in w:
            cumSum += weight
        accumSum = 0
        for weight in w:
            accumSum += weight/cumSum
            self.cumulativeSum.append(accumSum)

    def pickIndex(self):
        target = random.random()
        return bisect.bisect_left(self.cumulativeSum, target)
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
