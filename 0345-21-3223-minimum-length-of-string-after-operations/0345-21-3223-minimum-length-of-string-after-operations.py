class Solution:
    def minimumLength(self, s: str) -> int:
        d = Counter(s)
        res = 0
        for v in d.values():
            if v%2 == 1:
                res += v - 1
            else:
                res += v - 2
        
        return len(s) - res
