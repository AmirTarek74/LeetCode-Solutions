class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        y = 0
        x = 0
        res = 0
        n = len(s)
        for i in range(n):
            if s[i] == "N":
                y += 1
            elif s[i] == "S":
                y -= 1
            elif s[i] == "E":
                x += 1
            else:
                x -= 1
            res = max(res, min(abs(x) + abs(y) + k *2, i + 1))
        return res
