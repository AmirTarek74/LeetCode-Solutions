class Solution:
    def averageValue(self, nums: List[int]) -> int:
        res = []
        
        for num in nums:
            if num%6==0:
                res.append(num)
        if len(res):
            return floor(sum(res)/len(res))
        else: 
            return 0