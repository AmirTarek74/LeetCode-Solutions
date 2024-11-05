class Solution:
    def minChanges(self, s: str) -> int:
        lst = [s[i:i+2] for i in range(0,len(s),2)]
        res = 0
        for item in lst:
            if item[0] != item[1]:
                res += 1
        
        return res