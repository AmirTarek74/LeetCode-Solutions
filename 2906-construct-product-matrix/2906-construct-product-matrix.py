class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        
        n,m = len(grid), len(grid[0])
        
        prefix = [1]
        suffix = [1]
        
        for r in range(n):
            for c in range(m):
                prefix.append((prefix[-1]*grid[r][c])%12345)
        
        for r in reversed(range(n)):
            for c in reversed(range(m)):
                suffix.append((suffix[-1]*grid[r][c])%12345)
                
        for i,j in product(range(n),range(m)):
            k = i*m + j
            grid[i][j] = (prefix[k]*suffix[-k-2])%12345
            
        return grid