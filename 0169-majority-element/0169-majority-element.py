class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        for i in nums:
            if i not in list(d.keys()):
                d[i]=1
            else:
                d[i]+=1
            
        d2 = sorted(d.items(), key=lambda x:x[1],reverse=True)
        return d2[0][0]