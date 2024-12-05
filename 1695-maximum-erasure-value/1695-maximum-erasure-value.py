class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        res = 0
        summa = 0
        l = 0
        visited = set()
        for i in range(len(nums)):
            if nums[i] not in visited:
                summa += nums[i]
                res = max(res, summa)
                visited.add(nums[i])
            else:
                while nums[i] in visited and l<i:
                    visited.remove(nums[l])
                    summa -= nums[l]
                    
                    l += 1
                summa += nums[i]
                visited.add(nums[i])
                res = max(res, summa)
        return res
        