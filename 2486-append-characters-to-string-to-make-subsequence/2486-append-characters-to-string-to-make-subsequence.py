class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        first = 0
        prefix =0 
        while first<len(s) and prefix <len(t):
            if s[first]==t[prefix]:
                prefix+=1
            first+=1
        return len(t)-prefix
        