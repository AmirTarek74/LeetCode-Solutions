class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d={}
        for n in nums:
            if n in d.keys():
                return n
            d[n] = 1
            
        return -1