class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        
        c = len(matrix[0])
        
        res = 0
        
        for r in matrix:
            flipped_row = [ 1 - x for x in r ]
            
            identical_row = sum(
                1 for c_r in matrix
                if c_r == r or c_r == flipped_row
            )
            
            res = max(res, identical_row)
        
        return res