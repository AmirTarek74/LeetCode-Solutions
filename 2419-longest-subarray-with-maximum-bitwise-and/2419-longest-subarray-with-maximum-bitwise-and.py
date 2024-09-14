class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
       
        max_val = max(nums)
        count = 0
        res = 0
        
        for num in nums:
            if max_val == num:
                count +=1
            else:
                count = 0
            
            res = max(res,count)
        
        return res
            
        