class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n,m = len(matrix), len(matrix[0])
        
        res = [[-1 for i in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                res[i][j] = matrix[j][i]
        
        return res
        