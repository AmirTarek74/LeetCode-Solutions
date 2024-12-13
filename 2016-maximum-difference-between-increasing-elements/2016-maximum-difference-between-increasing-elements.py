class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        res = -1
        mini = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i]<mini:
                mini = nums[i]
                continue
            res = max(res, nums[i]-mini)
        
        return res if res>0 else -1
        