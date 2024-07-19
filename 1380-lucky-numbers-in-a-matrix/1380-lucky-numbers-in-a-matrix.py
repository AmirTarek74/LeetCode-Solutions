import numpy as np
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        luckyNumbers = []
        matrix = np.array(matrix)
        m,n = matrix.shape
        
        for i in range(m):
            mini = min(matrix[i])
            for j in range(n):
                maxi = max(matrix[:,j])
                if matrix[i][j]==mini and matrix[i][j]==maxi:
                    luckyNumbers.append(int(matrix[i][j]))
        
        return luckyNumbers