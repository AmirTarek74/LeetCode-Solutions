class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        nums.sort()
        res = 0
        
        for i in range(len(nums)):
            low = self.lower(nums, i+1, len(nums)-1, lower- nums[i])
            high = self.lower(nums, i+1, len(nums)-1, upper- nums[i] + 1)
            res = res + (high - low)
        
        return res
    
    def lower(self, nums, low, high, curr):
        while low<=high:
            mid = (low + high)//2
            if nums[mid]>= curr:
                high = mid - 1
            else:
                low = mid + 1
        return low
    
        