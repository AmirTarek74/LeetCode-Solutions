class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        res = 0
        
        summa = 0
        l = 0
        r = 0
        num_to_idx = {}
        
        while r < len(nums):
            
            last_occ = num_to_idx.get(nums[r], -1)
            
            while l<= last_occ or r - l + 1 >k:
                summa -= nums[l]
                l += 1
            
            num_to_idx[nums[r]] = r
            summa += nums[r]
            if r - l + 1 == k:
                res = max(res, summa)
            r += 1
        
        return res