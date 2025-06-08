class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        n = len(grid)
        m = len(grid[0])
        def dfs(i, j):
            if not (0<=i<n) or not(0<=j<m) or grid[i][j] == \0\:
                return
            
            grid[i][j] = \0\
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        for i in range(n):
            for j in range(m):
                if grid[i][j]==\1\:
                    res += 1
                    dfs(i, j)
        
        return res