class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        dirs = [-1, 0, 1]
        
        m, n = len(grid), len(grid[0])
        
        q = deque()
        
        visit = [[False]*n for _ in range(m)]
        
        for i in range(m):
            
            visit[i][0]= True
            q.append((i,0,0))
        
        res = 0 
        while q:
            size = len(q)
            
            for _ in range(size):
                row, col, moves = q.popleft()
                res = max(res, moves)
                for d in dirs:
                    n_row = row + d
                    n_col = col + 1
                    
                    if (
                      0<=n_row<m 
                        and 0<=n_col<n
                        and not visit[n_row][n_col]
                        and grid[n_row][n_col]>grid[row][col]
                    ):
                        q.append((n_row, n_col, moves+1))
                        visit[n_row][n_col] = True
            
        return res
                        
                        
                