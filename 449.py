from collections import deque
class Codec:
    def serialize(self, root):
        if not root:
            return ''
        result = []
        queues = deque([root])
        while queues:
            currentNode = queues.popleft()
            if currentNode:
                result.append(str(currentNode.val))
                queues.extend([currentNode.left])
                queues.extend([currentNode.right])
            else:
                result.append("-")
        return ",".join(result)
    def deserialize(self, data):
        if not data:
            return None
        treeList = deque(data.split(','))
        rootNode = TreeNode(int(treeList.popleft()))
        queues = deque([rootNode])
        while queues:
            currentnode = queues.popleft()
            if (leftOne := treeList.popleft()) != "-":
                currentnode.left = TreeNode(int(leftOne))
                queues.append(currentnode.left)
            if (rightOne := treeList.popleft()) != "-":
                currentnode.right = TreeNode(int(rightOne))
                queues.append(currentnode.right)
        return rootNode

