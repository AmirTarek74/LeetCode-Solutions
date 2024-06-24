class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        out = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    out+=4
                    if i!=0:
                        if grid[i-1][j]==1:
                            out-=1
                    if i!=row-1:
                        if grid[i+1][j]==1:
                            out-=1
                    if j!=0:
                        if grid[i][j-1]==1:
                            out-=1
                    if j!=col-1:
                        if grid[i][j+1]==1:
                            out-=1
                    
                    
                     
                    

        return out