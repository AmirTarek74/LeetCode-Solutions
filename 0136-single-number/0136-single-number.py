class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        d = {}
        for i in range(len(nums)):
            if nums[i] not in list(d.keys()):
                d[nums[i]] = 0
            
            d[nums[i]] += 1
        
        for i in list(d.keys()):
            if d[i]==1:
                return i
        