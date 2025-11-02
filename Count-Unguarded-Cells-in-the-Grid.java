class Solution {
    
    public int countUnguarded(int m, int n, int[][] guards, int[][] walls) {
        int[][] grid = new int[m][n];
        for(int[] row: grid)
        {
            Arrays.fill(row, 0);
        }
        for(int[] g: guards)
        {
            grid[g[0]][g[1]] = 2;
        }
        for(int[] w:walls)
        {
            grid[w[0]][w[1]] = -1;
        }
        for(int[] g: guards)
        {
            markGuard(grid, g[0] - 1, g[1] , 'U');
            markGuard(grid, g[0] + 1, g[1] , 'D');
            markGuard(grid, g[0] , g[1] + 1 , 'R');
            markGuard(grid, g[0] , g[1] - 1 , 'L');
        }
        int res = 0;
         for(int i = 0; i< m; i++)
        {
            for (int j = 0; j<n ;j++)
            {
                if(grid[i][j] == 0) res++;
            }
        }
        
        return res;
    }
    private void markGuard(int[][] grid, int i, int j, char dir)
    {
        if(Math.min(i, j) < 0 || i >= grid.length || j >= grid[0].length || grid[i][j]==-1 || grid[i][j]==2) return;
        grid[i][j] = 1;
        if(dir == 'U') markGuard(grid, i - 1, j , 'U');
        else if (dir == 'D') markGuard(grid, i + 1, j , 'D');
        else if (dir == 'R')  markGuard(grid, i, j+1 , 'R');
        else
        markGuard(grid, i, j -1 , 'L');
        
    }
}