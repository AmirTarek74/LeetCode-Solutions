class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        o = min(s1,s2)
        I = max(s1,s2)
        
        for i in range(len(s1)):
            if o[i]<=I[i]:
                continue
            else:
                return False
        
        return True