class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        res = []
        
        for i in range(n-k+1):
            res.append(self.power(nums,i,k))
        
        return res
    
    
    def power(self, nums,i, k):
        
        
        for j in range(i+1,i+k):
            if nums[j]-1!=nums[j-1]:
                return -1
        
        return nums[i+k-1]
        