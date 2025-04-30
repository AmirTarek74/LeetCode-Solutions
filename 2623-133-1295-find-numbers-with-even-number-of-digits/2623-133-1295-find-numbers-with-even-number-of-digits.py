class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            s = str(n)
            if len(s)%2 == 0:
                res += 1
        return res