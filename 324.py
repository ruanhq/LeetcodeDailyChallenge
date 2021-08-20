#324. Wiggle Sort II:  
class Solution:
    def wiggleSort(self, nums):
    	#sorting in ascending order followed by pairwise swapping.
        nums.sort()
        #pairwise switch is done.
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
        return nums


class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        if leftDepth == rightDepth:
            return pow(2, leftDepth) + self.depthCount(root.right)
        else:
            return pow(2, rightDepth) + self.depthCount(root.left)
    def getDepth(self, root):
        if not root:
            return 0 
        return self.getDepth(root.left)

class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        if leftDepth == rightDepth:
            return pow(2, leftDepth) + self.countNodes(root.right)
        else:
            return pow(2, rightDepth) + self.countNodes(root.left)








