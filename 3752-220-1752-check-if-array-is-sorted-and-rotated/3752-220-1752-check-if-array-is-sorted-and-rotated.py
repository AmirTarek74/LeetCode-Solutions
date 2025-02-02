class Solution:
    def check(self, nums: List[int]) -> bool:
        violations = 0
        if nums[-1] > nums[0]:
            violations += 1
        
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                violations += 1
        
        return True if violations <= 1 else False
