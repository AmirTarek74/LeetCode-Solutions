class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        l = min(len(word1),len(word2))
        for i in range(l):
            res+= word1[i]
            res+= word2[i]
        if len(word1)<len(word2):
            res += word2[l:]
        elif len(word1)>len(word2):
            res += word1[l:]
        return res
        