class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def area(g, r, c, row, col):
            if r < 0 or c < 0 or r==row or c == col or g[r][c] != 1:
                return 0
            g[r][c]=2
            return 1+area(g, r+1, c,row,col)+area(g,r-1,c, row, col) \
            +area(g, r, c+1, row, col) + area(g, r,c-1, row, col)
        visited = set()
        row, col = len(grid), len(grid[0])
        res = 0
        
        
        for r in range(0, row):
            for c in range(0, col):
                if grid[r][c] == 1:
                    pass
                    res = max(res, area(grid, r, c , row, col))
        return res
