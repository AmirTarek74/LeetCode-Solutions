class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        op = 0
        
        for i in range(len(nums)-2):
            if nums[i]==0:
                op +=1
                for j in range(i,i+3):
                    if nums[j]==0:
                        nums[j] = 1
                    else:
                        nums[j]= 0
        
        
        if sum(nums) == len(nums):
            return op
        else:
            return -1