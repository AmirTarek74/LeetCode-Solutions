class Solution:
    def minLength(self, s: str) -> int:
        res = []
        
        i = 0
        while i<len(s):
            while res and  i<len(s) and ((res[-1]=='A' and s[i]=='B') or (res[-1]=='C' and s[i]=='D')):
                res.pop()
                i +=1
            if i>=len(s):
                return len(res)
            res.append(s[i])
            i+=1
        
        return len(res)
        