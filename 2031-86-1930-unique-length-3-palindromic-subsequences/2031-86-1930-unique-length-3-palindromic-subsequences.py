class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        letters = set(s)
        res =0

        for letter in letters:
            i, j = s.index(letter), s.rindex(letter)
            inbetween = set()
            for k in range(i+1, j):
                inbetween.add(s[k])
            res += len(inbetween)
        
        return res