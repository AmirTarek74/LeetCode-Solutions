class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        for c in s:
            if c.isalpha() or c.isdigit():
                new_s += c.lower()
        
        return new_s==new_s[::-1]