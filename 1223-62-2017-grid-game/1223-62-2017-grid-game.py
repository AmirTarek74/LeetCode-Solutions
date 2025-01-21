class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        first_row_sum = sum(grid[0])
        second_row_sum = 0
        min_sum  = float("inf")

        for idx in range(len(grid[0])):
            first_row_sum -= grid[0][idx]
            min_sum = min(min_sum, max(first_row_sum, second_row_sum))
            second_row_sum += grid[1][idx]
        
        return min_sum