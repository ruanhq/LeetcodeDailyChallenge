#889. Construct binary search tree from preorder and postorder:
class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val 
        self.left = None
        self.right = None 

class Solution:
    def constructFromPrePost(self, preorder, postorder):
        #for binary search problem, utilize a helper function here would help a lot!
        def helper(preOrderList, postOrderList):
            if not preOrderList:
                return None
            if len(preOrderList) == 1:
                return TreeNode(preOrderList[0])
            rootVal = postOrderList.pop()
            rootNode = TreeNode(rootVal)
            splitIndex = preOrderList.index(rootVal)
            rootNode.left = helper(preOrderList[1:splitIndex], postOrderList)
            rootNode.right = helper(preOrderList[splitIndex:], postOrderList)
            return rootNode
        return helper(preorder, postorder)

