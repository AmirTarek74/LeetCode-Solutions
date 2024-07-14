class Solution:
    def scoreOfString(self, s: str) -> int:
        summa = 0
        for idx in range(1,len(s)):
            summa += abs(ord(s[idx])-ord(s[idx-1]))
        return summa
            