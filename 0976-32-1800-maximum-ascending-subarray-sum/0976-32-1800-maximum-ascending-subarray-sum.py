class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        cur_sum = nums[0]
        for i in range(1, len(nums)):
            res = max(res, cur_sum)
            if nums[i] > nums[i-1]:
                cur_sum += nums[i]
            else:
                cur_sum = nums[i]
        res = max(res, cur_sum)   
        return res