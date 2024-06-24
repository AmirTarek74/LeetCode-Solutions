class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights,reverse=False)
        res = 0
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                res +=1
        return res