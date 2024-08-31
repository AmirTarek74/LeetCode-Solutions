class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        count = [0] * 26
        for i in range(len(s)):
            count[ord(t[i])-ord('a')] +=1
            
            count[ord(s[i])-ord('a')] -=1
            
        
        res = 0
        for i in range(26):
            res = res + max(0,count[i])
        
        return res