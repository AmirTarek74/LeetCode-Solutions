class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        output=[]
        target = 0
        s = set()
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while j<k:
                summa = nums[i] + nums[j]+nums[k]
                if summa==target:
                    s.add((nums[i],nums[j],nums[k]))
                    k-=1
                    j+=1
                elif summa<target:
                    j+=1
                else:
                    k-=1
        
        output = list(s)
        return output


        