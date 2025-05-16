class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        
        if x == 0 :
            return True
        
        rev = 0
        n = x
        while n:
            rev = rev * 10 + n % 10
            n = n // 10

        return x == rev 