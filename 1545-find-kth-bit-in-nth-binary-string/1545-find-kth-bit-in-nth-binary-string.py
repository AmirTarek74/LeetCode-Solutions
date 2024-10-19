class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        s = "0"
        
        for i in range(n-1):
            s = s + "1" + self.invert(s)[::-1]
        
        return s[k-1]
        
    def invert(self, s):
        res = ""
        for c in s:
            if c == '0':
                res += '1'
            else:
                res += '0'
        return res