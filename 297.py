import collections
class Codec:
    def serialize(self, root):
        listResult = []
        queue = collections.deque([root])
        while queue:
            currentNode = queue.pop()
            if currentNode:
                listResult.append(currentNode.val)
                queue.appendleft(currentNode.left)
                queue.appendleft(currentNode.right)
            else:
                listResult.append('')
        return ','.join(listResult)
    def reserialize(self, data):
        if not data:
            return 
        resultList = data.split(",")
        rootNode = TreeNode(resultList[0])
        queue = collections.deque([rootNode])
        i = 1
        while queue:
            currentNode = queue.pop()
            #go through its left child:
            if i < len(resultList) and resultList[i]:
                currentNode.left = TreeNode(resultList[i])
                queue.appendleft(currentNode.left)
            i += 1
            #go through its right child
            if i < len(resultList) and resultList[i]:
                currentNode.right = TreeNode(resultList[i])
                queue.appendleft(currentNode.right)
            i += 1
        return rootNode
