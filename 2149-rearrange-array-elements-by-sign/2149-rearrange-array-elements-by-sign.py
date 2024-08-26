class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        p_idx = 0
        n_idx = 1
        for n in nums:
            if n>0:
                res[p_idx]=n
                p_idx +=2
            else:
                res[n_idx]=n
                n_idx +=2
        
    
            
        return res