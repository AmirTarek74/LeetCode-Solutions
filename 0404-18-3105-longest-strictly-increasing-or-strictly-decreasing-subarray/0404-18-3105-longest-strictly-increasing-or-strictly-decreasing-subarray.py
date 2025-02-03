class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        is_increasing = True
        is_decreasing = True
        inc = 1
        dec = 1
        res1 = 0
        res2 = 0
        for i in range(len(nums)-1):
            if not is_increasing:
                inc = 1
                is_increasing = True
            if not is_decreasing:
                dec = 1
                is_decreasing = True
            if nums[i] > nums[i+1]:
                dec += 1
                is_increasing = False
            elif nums[i] < nums[i+1]:
                inc += 1
                is_decreasing = False
            else:
                is_decreasing = False
                is_increasing = False
            res1 = max(res1, inc)
            res2 = max(res2, dec)
        
        return max(res1, res2)