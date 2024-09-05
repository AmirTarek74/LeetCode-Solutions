class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        d = {}
        l = 0
        maxf = 0
        for i in range(len(s)):
            d[s[i]] = d.get(s[i],0) + 1
            
            maxf = max(maxf, d[s[i]])
            
            if (i-l+1)-maxf >k:
                d[s[l]] -=1
                l +=1
        
        return len(s)-l