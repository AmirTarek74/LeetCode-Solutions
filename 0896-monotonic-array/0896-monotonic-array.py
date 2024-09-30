class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = False
        dec = False
        
        i = 1
        while i<len(nums):
            if nums[i]<nums[0]:
                dec = True
                break
            elif nums[i]>nums[0]:
                inc = True
                break
            i+=1
        i = 1
        while i <len(nums) and inc:
            if nums[i]<nums[i-1]:
                return False
            i+=1
        
        while i <len(nums) and dec:
            if nums[i]>nums[i-1]:
                return False
            i+=1
        
        return True
        