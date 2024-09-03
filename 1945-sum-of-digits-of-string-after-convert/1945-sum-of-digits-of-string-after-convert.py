class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        res = ''
        for c in s:
            if c=='a':
                res +='1'
            else:
                res += str(ord(c)-ord('a') + 1)
        ans = 0
        for i in range(k):
            ans = 0
            for c in res:
                ans = ans + int(c)
            
            res = str(ans)
            
        
        return ans
        