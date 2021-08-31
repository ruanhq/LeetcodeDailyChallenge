#DFS version
class Solution:
    def numIslands(self, grid):
        if len(grid) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        #searching from the current position:
        def graphSearch(grid, i, j):
            if grid[i][j] == '0':
                return 
            grid[i][j] = '0'
            if i != 0 and grid[i - 1][j] == '1':
                graphSearch(grid, i - 1, j)
            if i != m - 1 and grid[i + 1][j] == '1':
                graphSearch(grid, i + 1, j)
            if j != 0 and grid[i][j - 1] == '1':
                graphSearch(grid, i, j - 1)
            if j != n - 1 and grid[i][j + 1] == '1':
                graphSearch(grid, i, j + 1)
        result = 0
        for i in range(m):
        	for j in range(n):
        	    if grid[i][j] == '1':
        	        graphSearch(grid, i, j)
        	        result += 1
        return result

#BFS version:
from collections import deque
class Solution:
    def numIslands(self, grid):
        result = 0
        if len(grid) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    self.bfsHelper(grid, i, j)
                    result += 1
    def bfsHelper(self, grid, i, j):
        queue = deque([(i, j)])
        while queue:
            i, j = queue.popleft()
            for i, j in [i + 1, j], [i, j + 1], [i - 1, j], [i, j - 1]:
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                    grid[i][j] = '0'
                    queue.append((i, j))

