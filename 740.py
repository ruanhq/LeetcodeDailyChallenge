#740. DeleteAndEarn:
#use dp and do the mapping of nums
from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counters = Counter(nums)
        freqMap = [0] * (max(nums) + 1)
        for c in counters:
            freqMap[c] = c * counters[c]
        for i in range(2, max(nums) + 1):
            freqMap[i] = max(freqMap[i - 2] + freqMap[i], freqMap[i - 1])
        return freqMap[-1]