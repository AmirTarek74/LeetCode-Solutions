class Solution:
    def makeFancyString(self, s: str) -> str:
        streak = 1
        res = [s[0]]
        for i in range(1, len(s)):
            if s[i]==s[i-1]:
                streak+=1
            else:
                streak = 1
            if streak < 3:
                res.append(s[i])
        
        return "".join(res)
                
        