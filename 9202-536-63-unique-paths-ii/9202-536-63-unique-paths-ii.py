class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m ==0 or n == 0:
            return 0
        if m == 1 and n == 1:
            return 1 if grid[0][0] == 0 else 0
        
        dp = [[0]* (n) for _ in range(m)]
        dp[0][0] = 0 if grid[0][0] == 1 else 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if i > 0 and j > 0:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
                    elif i >0 :
                        dp[i][j] = dp[i-1][j]
                    elif j > 0:
                        dp[i][j] = dp[i][j-1]
        return dp[-1][-1]