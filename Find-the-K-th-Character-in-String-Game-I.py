class Solution:
    def kthCharacter(self, k: int) -> str:
        s = "a"
        while len(s) < k:
            l = len(s)
            i = 0
            while len(s) < k and i < l:
                new_c = chr((ord(s[i]) + 1)) if s[i] != "Z" else "a"
                s+= new_c
                i += 1
        return s[k-1]
        
