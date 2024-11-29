class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        
        rows, cols = len(grid), len(grid[0])
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        
        pq = [[grid[0][0], 0, 0]]
        
        while pq:
            time, row, col = heapq.heappop(pq)
            
            if row == rows - 1 and col == cols - 1:
                return time
            
            if (row, col) in visited:
                continue
                
            visited.add((row, col))
            
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                
                if not self.is_valid(visited, new_row, new_col, rows, cols):
                    continue
                wait_time = (1 if (grid[new_row][new_col] - time ) %2 == 0 else 0)
                
                next_time = max(grid[new_row][new_col] + wait_time , time + 1)
                heapq.heappush(pq, (next_time, new_row, new_col))
        return -1
    
    
    def is_valid(self, visited, r, c, rows, cols):
        return 0 <= r < rows and 0 <= c < cols and (r, c) not in visited
        