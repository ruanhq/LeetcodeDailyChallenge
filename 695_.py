class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        seen = set()
        def area(i, j):
            if (i < 0 or i >= m or j < 0 or j >= n) or (i, j) in seen or grid[i][j] == 0:
                return 0
            seen.add((i, j))
            currentArea = 1 + area(i - 1, j) + area(i + 1, j) + area(i, j - 1) + area(i, j + 1)
            return currentArea
        areaDict = set()
        for i in range(m):
            for j in range(n):
                areaDict.add(area(i, j))
        return max(areaDict)
