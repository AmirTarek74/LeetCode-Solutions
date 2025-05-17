class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        seen = set()
        def dfs(i, j):
            if (i<0 or i >= rows) or (j < 0 or j >= cols) or (i,j) in seen:
                return
            matrix[i][j] = 0
            seen.add((i, j))
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)   
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0 and (i,j) not in seen:
                    x = i
                    y = 0
                    while y < cols:
                        if matrix[x][y] == 0:
                            y += 1
                            continue
                        matrix[x][y] = 0
                        seen.add((x, y))
                        y += 1
                    x = 0
                    y = j
                    while x < rows:
                        if matrix[x][y] == 0:
                            x += 1
                            continue
                        matrix[x][y] = 0
                        seen.add((x, y))
                        x += 1

