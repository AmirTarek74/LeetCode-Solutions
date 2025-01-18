class Solution:
    _dirs = [(0,1), (0, -1), (1,0), (-1,0)]
    def minCost(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])

        min_cost = [[float("inf")] * num_cols for _ in range(num_rows)]
        min_cost[0][0] = 0

        dq = collections.deque([(0,0)])

        while dq:
            row, col = dq.popleft()

            for dir_idx, (dx, dy) in enumerate(self._dirs):
                new_row, new_col = row+dx, col+dy
                cost = 0 if grid[row][col] == dir_idx + 1 else 1

                if (
                    self.is_valid(new_row, new_col, num_rows, num_cols) and
                        min_cost[row][col] + cost < min_cost[new_row][new_col]
                    ):
                    min_cost[new_row][new_col] = min_cost[row][col] + cost
                    if cost == 1:
                        dq.append((new_row, new_col))
                    else:
                        dq.appendleft((new_row, new_col))
        return min_cost[-1][-1]
    
    def is_valid(self, r, c, rows, cols):
        return 0<=r<rows and 0<=c < cols