#137. Missing Number:
class Solution:
    def singleNumber(nums):
        assumedSum = 3 * sum(set(nums))
        result = (sum(nums) - assumedSum) // 2
        return result
