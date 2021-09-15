class Solution:
    def minFlips(self, mat: List[List[int]]):
        nRow = len(mat)
        nCol = len(mat[0])
        initial = ''.join(str(cell) for row in mat for cell in row)
        targets = "0" * (nRow * nCol)
        flips = {'1': '0', '0': '1'}
        def flip(node, pos):
            node[pos] = flips[node[pos]]
            if pos % nCol != 0:
                left = pos - 1
                node[left] = flips[node[left]]
            if pos % nCol < nCol - 1:
                right = pos + 1 
                node[right] = flips[node[right]]
            if pos >= nCol:
                top = pos - nCol
                node[top] = flips[node[top]]
            if pos < (nRow - 1) * nCol:
                bottom = pos + nCol 
                node[bottom] = flips[node[bottom]]
        q = collections.deque([initial])
        result = 0
        visited = set()
        while q:
            for _ in range(len(q)):
                currentNode = q.popleft()
                if currentNode == target:
                    return result 
                if currentNode in visited:
                    continue
                visited.add(node)
                for i in range(len(currentNode)):
                    nextNode = list(currentNode)
                    flip(nextNode, i)
                    q.append(''.join(nextNode))
            result += 1
        return -1
