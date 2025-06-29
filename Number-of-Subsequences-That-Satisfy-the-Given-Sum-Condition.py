class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10**9 + 7
        
        nums.sort()
        res = 0
        if nums[0] > target:
            return 0
        l = 0
        r = len(nums) -1 
        while l <= r:
            if nums[l] + nums[r] <= target:
                res =  (res + 2**(r-l) ) % mod
                l += 1
            else:
                r -= 1
        return res
