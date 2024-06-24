class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        out = []
        nums.sort()
        d = Counter(nums)
        rep = -1
        missed= -1
        for i in range(1,len(nums)+1):
            if d[i]==2:
                rep = i
            elif d[i]==0:
                missed = i
        
            
       
        return [rep,missed]
        