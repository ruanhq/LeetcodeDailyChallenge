#191. Number of 1 Bits:
class Solution:
    def hammingWeight(self, n: int):
        count = 0
        while n != 0:
            n = n & (n - 1)
            count += 1
        return count