class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        
        res = float("inf")
        cur_sum = 0

        for right in range(0, len(nums)):
            cur_sum += nums[right]

            while cur_sum >= target:
                res = min(res, right-l + 1)
                cur_sum -= nums[l]
                l += 1
        
        return res if res != float("inf") else 0
        