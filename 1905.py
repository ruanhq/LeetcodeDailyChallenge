#1905. Count Sub Islands:
class Solution:
    def countSubIslands(self, grid1, grid2):
        m = len(grid1)
        n = len(grid1[0])
        def dfs(i, j):
            if (i >= m or i < 0 or j >= n or j < 0):
                return
            if grid2[i][j] == 0:
                return
            grid2[i][j] = 0
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
        if m == 0 or n == 0:
            return 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    dfs(i, j)
        result = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    dfs(i, j)
                    result += 1
        return result
