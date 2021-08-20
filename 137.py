#137. Missing Number:
class Solution:
    def singleNumber(nums):
        if len(nums) == 1:
            return nums
        result = 0
        for i in range(32):
        	sums = 0
        	for num in nums:
        	    sums += (nums >> i) & 1
        	    sums %= 3
        	result = result | (sums << i)
        return res
    ########
    ########
    ########
    ########
    def singleNumber(nums):
        if len(nums) == 1:
            return nums
        result = 0 
        for i in range(32):
            sums = 0 
            for num in nums:
                sums += (nums >> i) & 1
                sums %= 3
            result = result | (sums << i)
        return result

    def singleNumber(nums):
        if len(nums) == 1:
            return nums[0]
        result = 0
        for i in range(32):
            sums = 0
            for num in nums:
                sums += (num >> i) & 1
                sums %= 3
            result = result | (sums << i)
        return result