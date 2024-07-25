class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<2:
            return nums
        
        midpoint = len(nums)//2
        
        return self.merge(left=self.sortArray(nums[:midpoint]),
                         right =self.sortArray(nums[midpoint:]))
    
    def merge(self, left, right):
        if len(left)==0:
            return right
        if len(right)==0:
            return left
        
        result = []
        left_idx = right_idx = 0
        
        while(len(result)< len(left)+len(right)):
            
            if left[left_idx]< right[right_idx]:
                result.append(left[left_idx])
                left_idx +=1
            else:
                result.append(right[right_idx])
                right_idx +=1
                
            if right_idx==len(right):
                result += left[left_idx:]
                break
                
            if left_idx == len(left):
                result += right[right_idx:]
                break
        
        return result