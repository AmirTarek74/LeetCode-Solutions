class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n==0 :
            return 1
        one = False
        for i in range(n):
            if nums[i]==1:
                one = True
            if nums[i]>n or nums[i]<=0:
                nums[i] = 1
        if not one:
            return 1
        for i in range(n):
            
            nums[abs(nums[i])-1] = -1 * abs(nums[abs(nums[i])-1])
                
        for i in range(n):
            if nums[i]>0:
                return i+1
            
        return n+1