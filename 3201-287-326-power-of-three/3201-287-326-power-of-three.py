class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        res = 0
        while n > 3**res:
            res+= 1
        
        return 3**res == n