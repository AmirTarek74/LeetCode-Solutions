class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        if len(s) < 2:
            return False
        m = set()
        for i in range(len(s)-1, -1, -1):
            m.add(s[i-1:i+1][::-1])
        
        for i in range(len(s)):
            if s[i:i+2] in m:
                return True
        return False