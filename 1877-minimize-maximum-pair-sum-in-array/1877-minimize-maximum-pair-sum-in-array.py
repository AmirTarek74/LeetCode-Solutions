class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0,len(nums)-1
        pair = []
        while l<r:
            pair.append([nums[l],nums[r]])
            l+=1
            r-=1
        
        maxi = float("-inf")
        
        for p in pair:
            maxi = max(maxi, sum(p))
        
        return maxi