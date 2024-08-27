class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        if len(nums)==1:
            return [nums[:]]
        
        for i in range(len(nums)):
            value = nums.pop(0)
            
            perms = self.permute(nums)
            
            for p in perms:
                p.append(value)
            res.extend(perms)
            nums.append(value)
        
        return res