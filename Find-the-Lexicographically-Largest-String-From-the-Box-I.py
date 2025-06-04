class Solution:
    def answerString(self, word: str, f: int) -> str:
        if f == 1:
            return word
        
        n = len(word)
        res = ""
        for i in range(n):
            res = max(res, word[i: min(i + n -f + 1, n)])
        return res