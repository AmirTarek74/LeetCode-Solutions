class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        d = {}
        res = 0
        
        for i in range(len(s)):
            d[s[i]] = d.get(s[i],0) + 1
            while d and d[s[i]]>1:
                
                d[s[l]] -=1
                l+=1
            
            res = max(res, i-l+1)
        
        return res
            