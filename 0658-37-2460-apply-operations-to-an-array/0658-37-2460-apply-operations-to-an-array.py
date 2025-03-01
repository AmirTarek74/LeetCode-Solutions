class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        zero_idx = 0
        
        while zero_idx < len(nums) :
            while zero_idx < len(nums) and nums[zero_idx]!= 0:
                zero_idx += 1
            nonzero_idx = zero_idx
            while nonzero_idx < len(nums) and nums[nonzero_idx]== 0:
                nonzero_idx += 1
            if zero_idx < len(nums) and  nonzero_idx < len(nums):
                nums[zero_idx], nums[nonzero_idx] = nums[nonzero_idx], nums[zero_idx]
            else:
                break
        
        return nums
        