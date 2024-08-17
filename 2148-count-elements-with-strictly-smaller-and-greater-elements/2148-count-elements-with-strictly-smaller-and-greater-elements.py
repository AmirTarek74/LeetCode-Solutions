class Solution:
    def countElements(self, nums: List[int]) -> int:
        count = 0
        nums.sort()
        
        for i in range(1,len(nums)-1):
            idx = 0
            flag = False
            while idx<i:
                if nums[i]>nums[idx]:
                    flag = True
                    break
                idx+=1
            idx = i + 1
            while idx!=len(nums):
                if nums[i]<nums[idx]:
                    if flag==True:
                        count+=1
                    break
                idx+=1
        
        return count
        