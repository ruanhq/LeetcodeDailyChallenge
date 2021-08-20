#280. wiggleSort:
class Solution:
    def wiggleSort(self, nums):
        n = len(nums)
        if n == 1:
            return nums 
        indicatorLarge = 1
        for i in range(n - 1):
            if indicatorLarge == 1:
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            else:
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            indicatorLarge *= -1
        