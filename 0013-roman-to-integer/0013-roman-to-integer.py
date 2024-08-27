class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100,'D':500, 'M':1000}
        i = 0
        res = 0
        while i<len(s):
            if s[i]=='I' and i<len(s)-1 :
                if s[i+1] in ['V','X']:
                    temp = d[s[i+1]]-d[s[i]]
                    res += temp
                    i += 2
                else:
                    res += d[s[i]]
                    i += 1
                    
            elif s[i]=='X' and i<len(s)-1:
                if s[i+1] in ['L','C']:
                    temp = d[s[i+1]]-d[s[i]]
                    res += temp
                    i += 2
                else:
                    res += d[s[i]]
                    i += 1
            elif s[i]=='C' and i<len(s)-1:
                if s[i+1] in ['D','M']:
                    temp = d[s[i+1]]-d[s[i]]
                    res += temp
                    i += 2
                else:
                    res += d[s[i]]
                    i += 1
            else:
                res += d[s[i]]
                i += 1
        
        return res