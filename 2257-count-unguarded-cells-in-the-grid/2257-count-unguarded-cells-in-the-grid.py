class Solution:
    
    def _mark_guard(self, i, j, grid):
        
        for r in range(i-1, -1, -1):
            if grid[r][j] == 3 or grid[r][j]==2:
                break
            grid[r][j] = 1
        
        for r in range(i+1, len(grid)):
            if grid[r][j] == 3 or grid[r][j]==2:
                break
            grid[r][j] = 1
            
        for c in range(j-1, -1, -1):
            if grid[i][c] == 3 or grid[i][c]==2:
                break
            grid[i][c] = 1
        
        for c in range(j+1,len(grid[0])):
            if grid[i][c] == 3 or grid[i][c]==2:
                break
            grid[i][c] = 1
    
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0]*n for _ in range(m)]
        
        for g in guards:
            grid[g[0]][g[1]] = 2
        
        for w in walls:
            grid[w[0]][w[1]] = 3
        
        for g in guards:
            self._mark_guard(g[0], g[1], grid)
        
        res = 0 
        for row in grid:
            for cell in row:
                if cell == 0:
                    res += 1
        
        return res
        
        
        