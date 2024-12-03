class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        res = ""
        spaces = set(spaces)
        i = 0 
        while i < len(s):
            if i in spaces:
                res += ' '
                spaces.remove(i)
            else:
                res += s[i]
                i += 1
        
        return res