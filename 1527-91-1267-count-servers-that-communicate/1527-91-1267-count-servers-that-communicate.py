class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        if not grid:
            return  0
        
        rows_count = [0] * len(grid[0])
        cols_counts = [0] * len(grid)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    rows_count[c] += 1
                    cols_counts[r] += 1
        
        res = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    if rows_count[c] > 1 or cols_counts[r] > 1 :
                        res += 1

        return res