class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        res = float("inf")
        for i in range(len(nums)):
            temp = 0
            for j in range(i, min(i+r, len(nums))):
                temp += nums[j]
                if j-i+1 >=l and j-i+1 <= r and temp >0:
                    res = min(res, temp)
                
        
        return res if res != float("inf") else -1