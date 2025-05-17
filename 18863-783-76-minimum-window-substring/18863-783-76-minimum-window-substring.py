class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s
        if len(t) > len(s):
            return ""
        d1 = {}
        remaining = set()
        for c in t:
            d1[c] = d1.get(c, 0) + 1
            remaining.add(c)
        
        d2 = {}
        l = 0
        length = float("inf")
        res = ""
        for r in range(len(s)):
            d2[s[r]] = d2.get(s[r], 0) + 1
            if s[r] in d1 and d2[s[r]] >= d1[s[r]]:
                if s[r] in remaining:
                    remaining.remove(s[r])
            while l <= r and len(remaining) == 0:
                if r - l + 1 < length:
                    length = r - l + 1
                    res = s[l:r+1]
                d2[s[l]] = d2.get(s[l], 0) - 1
                if s[l] in d1 and d2[s[l]] < d1[s[l]]:
                    remaining.add(s[l])
                l += 1
        return res
                
                
