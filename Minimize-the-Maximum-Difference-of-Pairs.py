class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        res = 0
        
        def isvalid(diff):
            i = 1
            cnt = 0
            while i < len(nums):
                if nums[i] - nums[i-1] <= diff:
                    cnt += 1
                    i += 1
                i += 1
            
            return cnt >= p
        
        l = 0
        r = nums[-1]
        while l <= r:
            mid = (l + r) // 2
            if isvalid(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
            
        return res