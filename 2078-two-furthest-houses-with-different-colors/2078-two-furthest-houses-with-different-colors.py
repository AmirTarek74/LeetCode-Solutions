class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        res = 0
        for i,c in enumerate(colors):
            if c != colors[0]:
                res = max(res, i)
            if c != colors[-1]:
                res = max(res, len(colors) - 1 - i)
        
        return res
        
        