class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = abs(nums[-1]-nums[0])
        for i in range(1, len(nums)):
            res = max(res, abs(nums[i]- nums[i-1]))
        
        return res