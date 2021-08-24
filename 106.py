#106. Construct Binary Tree from Inorder and Postorder Traversal

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        rootVal = postorder.pop()
        rootNode = TreeNode(rootVal)
        rootIndex = inorder.index(rootNode.val)
        rootNode.right=self.buildTree(inorder[rootIndex+1:],postorder)
        rootNode.left=self.buildTree(inorder[:rootIndex],postorder)
        return rootNode
