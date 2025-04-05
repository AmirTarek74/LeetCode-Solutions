class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        def gen_seq(nums, index, subset, subsets):
            if index == len(nums):
                subsets.append(subset[:])
                return
            
            subset.append(nums[index])
            gen_seq(nums, index+1, subset, subsets)
            subset.pop()
            gen_seq(nums, index+1, subset, subsets)
        
        subsets = []
        gen_seq(nums, 0, [], subsets)
        
        res = 0
        for subset in subsets:
            sub_total = 0
            for n in subset:
                sub_total ^= n
            res += sub_total
        
        return res