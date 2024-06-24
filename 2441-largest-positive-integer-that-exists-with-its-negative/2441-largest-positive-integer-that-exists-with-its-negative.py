class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lst = sorted(nums,reverse=True)
        idx = 0
        while(idx<len(nums)):
            if -1*lst[idx] in nums:
                return lst[idx]
            idx+=1
        
        return -1
        