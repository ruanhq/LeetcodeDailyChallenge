# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getSplit(self, target, list):
        for i in range(len(list)):
            if list[i] > target:
                return i 
        return -1
    def bstFromPreorder(self, preorder):
        if not preorder:
            return None
        rootNode = TreeNode(preorder[0])
        splitIndex = self.getSplit(preorder[0], preorder)
        if splitIndex < 0:
            rootNode.left = self.bstFromPreorder(preorder[1:])
        else:
            rootNode.left = self.bstFromPreorder(preorder[1:splitIndex])
            rootNode.right = self.bstFromPreorder(preorder[splitIndex:])
        return rootNode
