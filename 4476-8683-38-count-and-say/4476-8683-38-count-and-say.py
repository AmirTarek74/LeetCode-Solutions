class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        if n == 1 :
            return res
        
        for i in range(1, n):
            res = self.RLE(res)
        
        return res
    
    def RLE(self, s):
        output = ""
        if len(s) == 1:
            return "1" + s
        cnt = 1
        idx = 1
        n = len(s)
        while idx < n:
            if s[idx] == s[idx-1]:
                cnt += 1
            else:
                output += str(cnt) + s[idx-1]
                cnt = 1
            idx += 1
        output += str(cnt) + s[idx-1]   
        return output