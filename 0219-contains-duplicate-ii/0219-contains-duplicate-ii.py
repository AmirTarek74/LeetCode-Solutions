class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            
            if d.get(nums[i],0)==0:
                d[nums[i]] = i+1
            else:
                if abs(d[nums[i]] - (i+1))<=k:
                    return True
                else:
                    d[nums[i]] = i+1
        return False