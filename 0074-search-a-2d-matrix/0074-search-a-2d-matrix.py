class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows, cols = len(matrix),len(matrix[0])
        
        top, bot = 0, rows-1
        
        while top<=bot:
            row = (bot + top)//2
            
            if target>matrix[row][-1]:
                top = row + 1
            elif target<matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if top>bot:
            return False
        
        row = (bot + top)//2
        l,r = 0, cols-1
        
        while l<=r:
            mid = (l+r)//2
            
            if matrix[row][mid]>target:
                r = mid - 1
            elif matrix[row][mid]<target:
                l = mid + 1
            else:
                return True
        
        return False
            
            
        