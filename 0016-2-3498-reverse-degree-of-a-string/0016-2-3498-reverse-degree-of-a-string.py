class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i,c in enumerate(s):
            res += (ord("z") - ord(c)+1) * (i+1)
        return res