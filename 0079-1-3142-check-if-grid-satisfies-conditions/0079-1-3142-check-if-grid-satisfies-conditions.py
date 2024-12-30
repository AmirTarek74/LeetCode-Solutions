class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:

        m,n = len(grid), len(grid[0])

        for r in range(m):
            for c in range(n):
                if r<m-1 and grid[r][c] != grid[r+1][c]:
                    return False
                elif c < n-1 and grid[r][c] == grid[r][c+1]:
                    return False
        
        return True
        