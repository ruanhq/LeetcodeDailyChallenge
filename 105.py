#105. Construct Binary Tree from Preorder and Inorder Traversal
#Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
#The main idea is to find the root node from the preorder traversal and do a recursive searching to construct the tree from the node.
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        root = preorder[0]
        del preorder[0]
        #How can you extract the left node?
        #two lists
        indexOfRoot = inorder.index(root)
        rootNode = TreeNode(inorder[indexOfRoot])
        rootNode.left = self.buildTree(preorder, inorder[:indexOfRoot])
        rootNode.right = self.buildTree(preorder, inorder[(indexOfRoot + 1):])
        return rootNode
