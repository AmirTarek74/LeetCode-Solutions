class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        
        for c in s:
            d[c] = d.get(c,0) + 1
        
        i = 0
        key = list(d.keys())
        for i in range(len(key)):
            if d[key[i]]==1:
                return s.find(key[i])
        
        return -1