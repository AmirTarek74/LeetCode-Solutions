class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        count = 0
        m = len(grid)
        n = len(grid[0])
        
        for row in range(m-2):
            for col in range(n-2):
                
                if self.IsMagic(grid,row,col):
                    count += 1
        
        return count
    
    
    def IsMagic(self, grid, row, col):
        
        visited = [0] * 10
        
        for i in range(3):
            for j in range(3):
                number = grid[row+i][col+j]
                if number < 1 or number>9:
                    return False
                if visited[number]:
                    return False
                
                visited[number] = 1
                
        
        dag1 = grid[row][col] + grid[row+1][col+1] + grid[row+2][col+2]
        dag2 = grid[row][col+2] + grid[row+1][col+1] + grid[row+2][col]
        
        if dag1 != dag2:
            return False
        
        row1 = grid[row][col] + grid[row][col+1] + grid[row][col+2]
        row2 = grid[row+1][col] + grid[row+1][col+1] + grid[row+1][col+2]
        row3 = grid[row+2][col] + grid[row+2][col+1] + grid[row+2][col+2]
        
        if not (row1==dag1 and row2 == dag1 and row3==dag1):
            return False
        
        
        col1 = grid[row][col] + grid[row+1][col] + grid[row+2][col]
        col2 = grid[row][col+1] + grid[row+1][col+1] + grid[row+2][col+1]
        col3 = grid[row][col+2] + grid[row+1][col+2] + grid[row+2][col+2]
        
        if not (col1==dag1 and col2 == dag1 and col3==dag1):
            return False
        return True
        
        
        
        
        
        
        
        
        