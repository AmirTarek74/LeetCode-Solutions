class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = []
        ans = 0
        for c in s:
            if c=='(':
                res.append('(')
            elif c==')' and res:
                res.pop()
            else:
                ans +=1
        
        return len(res) + ans