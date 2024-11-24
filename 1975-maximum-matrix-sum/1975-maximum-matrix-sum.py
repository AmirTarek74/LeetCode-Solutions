class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        
        summa = 0
        min_val = float("inf")
        neg_count = 0
        
        for row in matrix:
            for c in row:
                summa += abs(c)
                if c < 0 :
                    neg_count += 1
                
                min_val = min(min_val, abs(c))
        
        if neg_count %2 != 0 :
            summa -= 2 * min_val 
        
        return summa
        