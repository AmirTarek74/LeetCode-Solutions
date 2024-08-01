class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for num in nums:
            if d.get(num,0)==0:
                d[num] = d.get(num,0) + 1
            else:
                return True
        
        return False
        