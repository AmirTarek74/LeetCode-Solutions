class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            if i%2==0:
                if nums[i]%2 == 0:
                    continue
                else:
                    temp = i+1
                    while temp<len(nums):
                        if nums[temp]%2==0:
                            nums[i] , nums[temp] = nums[temp], nums[i]
                            break
                        else:
                            temp +=1
            
            else:
                if nums[i]%2 != 0:
                    continue
                else:
                    temp = i+1
                    while temp<len(nums):
                        if nums[temp]%2!=0:
                            nums[i] , nums[temp] = nums[temp], nums[i]
                            break
                        else:
                            temp+=1
        
        return nums
                    
        