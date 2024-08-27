class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
                
        m,n = len(board), len(board[0])
        for i in [0,m-1]:
            for j in range(n):
                self.dfs(board,i,j)
        for i in range(m):
            for j in [0,n-1]:
                self.dfs(board,i,j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=='.':
                    board[i][j]='O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        
        
    def dfs(self,board,i,j):
            if (0<=i<len(board) and 0<=j<len(board[0]) and board[i][j]=='O'):
                board[i][j]='.'
                self.dfs(board,i+1,j)
                self.dfs(board,i-1,j)
                self.dfs(board,i,j+1)
                self.dfs(board,i,j-1)
                