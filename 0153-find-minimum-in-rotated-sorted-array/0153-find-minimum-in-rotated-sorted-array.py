class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        mini = float("inf")
        
        while l<=r:
            mid = l + (r - l)//2
            mini = min(mini, nums[mid])
            
            if nums[mid]>nums[r]:
                l = mid + 1
            elif nums[mid]<nums[r]:
                r = mid - 1
            else:
                break
        
        return mini
                
                    
                
        