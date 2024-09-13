class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        res = []
        nums.sort()
        while nums:
            n1 = nums.pop(0)
            n2 = nums.pop()
            res.append((n1+n2)/2)
        
        return len(set(res))
        