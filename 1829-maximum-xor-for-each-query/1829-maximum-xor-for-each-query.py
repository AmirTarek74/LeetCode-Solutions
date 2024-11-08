class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
        res = []
        max_v = 2**maximumBit - 1
        l = len(nums)
        xored = 0
        for n in nums:
            xored = xored ^ n
        
        for _ in range(l):
            res.append(max_v ^ xored)
            xored = xored ^ nums[-1]
            nums.pop()
        return res
        