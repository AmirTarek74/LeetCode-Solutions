class Solution:
    class Cell:
        def __init__(self, height, row, col):
            self.height = height
            self.row = row
            self.col = col

        def __lt__(self, other):
            return self.height  < other.height
    
    def _isvalid(self, row, col, num_rows, num_cols):
        return 0<=row<num_rows and 0<= col < num_cols
    
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        dirs =[(0,-1), (0, 1), (-1, 0), (1, 0)]

        num_rows = len(heightMap)
        num_cols = len(heightMap[0])

        visited = [[False] * num_cols for _ in range(num_rows)]

        bonudary = []

        for i in range(num_rows):
            heapq.heappush(bonudary, self.Cell(heightMap[i][0], i, 0))
            heapq.heappush(bonudary, 
                    self.Cell(heightMap[i][num_cols-1], i, num_cols - 1)
                )
            visited[i][0] = visited[i][num_cols - 1] = True

        for i in range(1, num_cols-1):
            heapq.heappush(bonudary, self.Cell(heightMap[0][i], 0, i))
            heapq.heappush(bonudary, 
                    self.Cell(heightMap[num_rows - 1][i], num_rows - 1,  i)
                )
            visited[0][i] = visited[num_rows - 1][i] = True
        

        res = 0
        
        while bonudary:
            current_cell = heapq.heappop(bonudary)
            current_row = current_cell.row
            current_col = current_cell.col
            min_height = current_cell.height 

            for d in dirs:
                next_row = current_row + d[0]
                next_col = current_col + d[1]

                if (self._isvalid(next_row, next_col, num_rows, num_cols) and not visited[next_row][next_col]):
                    neighbour_height = heightMap[next_row][next_col]
                
                    if neighbour_height < min_height:
                        res += (min_height - neighbour_height)

                    heapq.heappush(bonudary, self.Cell(max(neighbour_height,min_height), 
                        next_row, next_col
                        )
                    )
                    visited[next_row][next_col] = True
        return res


        