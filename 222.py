#222. Count Complete Tree Nodes:
class Solution:
	def depthCount(self, root):
	    if not root:
	        return 0
	    return self.depthCount(root.left) + 1
	#Complete binary tree: the higher layer should be complete and the last layer is as left as possible
    def countNodes(self, root):
	    if not root:
	        return 0
	    leftDepth = self.depthCount(root.left)
	    rightDepth = self.depthCount(root.right)
	    ## left tree is complete, right tree can be complete
	    if leftDepth == rightDepth:
	        return 2 ** leftDepth + self.countNodes(root.right)
	    ## right tree is complete here, left tree can be not complete
	    else:
	        return 2 ** rightDepth + self.countNodes(root.left)