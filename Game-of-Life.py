class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        \\\
        Do not return anything, modify board in-place instead.
        \\\
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        r = len(board)
        c = len(board[0])

        for i in range(r):
            for j in range(c):
                live = 0
                for x, y in dirs:
                    if (0<= i + x < r) and (0<= j+y <c) and (abs(board[i+x][j+y])==1):
                        live += 1
                
                if board[i][j] == 1 and (live <2 or live > 3):
                    board[i][j] = -1 
                if board[i][j] == 0 and live == 3:
                    board[i][j] = 2
        
        for i in range(r):
            for j in range(c):
                board[i][j] = 1 if board[i][j] > 0 else 0
        return board