class Solution:
    def maxDifference(self, s: str) -> int:
        counter = {}
        for c in s:
            counter[c] = counter.get(c, 0) + 1
        
        a1 = 0
        a2 = float("inf")
        for k in counter:
            if counter[k] %2 ==0:
                a2 = min(a2, counter[k])
            else:
                a1 = max(a1, counter[k])
        
        return a1 - a2