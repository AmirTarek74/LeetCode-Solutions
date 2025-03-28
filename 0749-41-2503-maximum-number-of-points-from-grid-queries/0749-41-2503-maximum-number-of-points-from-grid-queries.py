from queue import PriorityQueue
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        
        res = [0] * len(queries)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        sorted_q = sorted([(val, idx) for idx, val in enumerate(queries)])

        min_heap = PriorityQueue()
        
        visited = [[False] * cols for _ in range(rows)]

        points = 0
        min_heap.put((grid[0][0], 0, 0))
        visited[0][0] = True
        for q, idx in sorted_q:
            while not min_heap.empty() and min_heap.queue[0][0] < q:
                val, r, c = min_heap.get()
                points += 1
                for dir in dirs:
                    new_r = r + dir[0]
                    new_c = c + dir[1]
                    if (
                        0 <= new_r < rows 
                        and 0 <= new_c < cols
                        and not visited[new_r][new_c]
                    ):
                        min_heap.put((grid[new_r][new_c], new_r, new_c))
                        visited[new_r][new_c] = True
            res[idx] = points
        
        return res