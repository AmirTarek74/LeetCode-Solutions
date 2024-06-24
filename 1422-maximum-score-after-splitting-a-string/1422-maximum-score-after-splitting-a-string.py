class Solution:
    def maxScore(self, s: str) -> int:
        lst=[]
        for i in range(1,len(s)):
            
            
            lst.append(s[:i].count('0')+s[i:].count('1'))
        
        return max(lst)
        