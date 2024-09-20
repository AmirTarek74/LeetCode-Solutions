class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s== "" or len(s)==1:
            return s
        
        l = 0
        for r in range(len(s)-1,-1,-1):
            if s[l] == s[r]:
                l +=1
        
        if l == len(s):
            return s
        
        non_pal = s[l:]
        reverse = non_pal[::-1]
        
        return (reverse + self.shortestPalindrome(s[0:l]) + non_pal)

        