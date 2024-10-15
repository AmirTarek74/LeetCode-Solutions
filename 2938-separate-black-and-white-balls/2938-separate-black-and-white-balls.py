class Solution:
    def minimumSteps(self, s: str) -> int:
        
        r = len(s) - 1
        res = 0
        s = [c for c in s]
        c = 0
        while r>=0:
            if s[r]=='0':
                c+=1
            else:
                res +=c
                #c = 0
            r -= 1 
        return res
                