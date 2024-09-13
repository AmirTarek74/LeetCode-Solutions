class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        
        res = 0 
        pos = 0
        for n in nums:
            pos += n
            if pos==0:
                res+=1
        
        return res