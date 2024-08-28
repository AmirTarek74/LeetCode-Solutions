class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        res = 0
        
        def dfs(i,j,c):
            if (i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!=1):
                return 0
            grid[i][j] = 0
            c += 1
            c = max(dfs(i+1,j,c),c) 
            c = max(dfs(i-1,j,c),c) 
            c = max(dfs(i,j+1,c),c) 
            c = max(dfs(i,j-1,c),c) 
            return c
            
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    
                    res = max(res,dfs(i,j,0))
                    
        return res