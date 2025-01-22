class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        rows = len(isWater)
        cols = len(isWater[0])

        cell_heights = [[-1] * cols for _ in range(rows)]

        q = deque()

        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:
                    cell_heights[r][c] = 0
                    q.append((r,c))
        
        next_height = 1
        while q:
            layer_size = len(q)

            for _ in range(layer_size):
                cur_row, cur_col = q.popleft()

                for d in dirs:
                    new_row = cur_row + d[0]
                    new_col = cur_col + d[1]
                    
                    if (self.is_valid(new_row, new_col, rows, cols) 
                        and cell_heights[new_row][new_col] == -1):
                        cell_heights[new_row][new_col] = next_height
                        q.append((new_row, new_col))

            next_height  += 1
        
        return cell_heights
    
    def is_valid(self, r, c, rows, cols):
        return 0 <= r < rows and 0 <= c < cols

