class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        def is_valid(row, col):
            return 0 <= row <  len(grid) and 0 <= col < len(grid[0])
        
        n, m = len(grid), len(grid[0])
        
        min_ob = [[float("inf")]* m for _ in range(n)]
        
        min_ob[0][0] = grid[0][0]
        
        pq = [[min_ob[0][0], 0, 0]]
        
        while pq:
            ob, row, col = heapq.heappop(pq)
            
            if row == n - 1 and col == m - 1 :
                return ob
            
            for d in directions:
                new_r = row + d[0]
                new_c = col + d[1]
                
                if is_valid(new_r, new_c):
                    
                    new_ob = ob + grid[new_r][new_c]
                    
                    if new_ob < min_ob[new_r][new_c]:
                        min_ob[new_r][new_c] = new_ob
                        heapq.heappush(pq, [new_ob, new_r, new_c])
            
        return min_ob[n-1][m-1]
        