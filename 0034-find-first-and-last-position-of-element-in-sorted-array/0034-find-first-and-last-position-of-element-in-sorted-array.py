class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        l,r = 0, len(nums)-1
        res = []
        
        while l<=r:
            mid = (l+r)//2
            
            if nums[mid]==target:
                
                idx = mid - 1
                while idx>=0 and nums[idx]==target:
                    idx-=1
                res.append(idx+1)    
                idx = mid
                while idx<len(nums) and nums[idx]==target:
                    idx+=1
                res.append(idx-1)
                return res
            elif nums[mid]>target:
                r = mid - 1
            else:
                l = mid + 1
        
        return [-1,-1]