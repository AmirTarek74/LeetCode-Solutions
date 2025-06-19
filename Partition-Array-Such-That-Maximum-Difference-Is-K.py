class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        idx = 0
        n = len(nums)
        temp = 0
        while idx < n:
            temp = nums[idx]
            idx += 1
            while idx < n and nums[idx]-temp <= k:
                idx += 1
            res += 1
        return res
            
            