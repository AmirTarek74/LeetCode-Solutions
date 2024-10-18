class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or_val = 0
        
        for n in nums:
            max_or_val |= n
        
        return self._count(nums,0,0,max_or_val)
    
    
    def _count(self,arr,i,cur_val,target):
        
        if i == len(arr):
            return 1 if cur_val==target else 0
        
        count_without = self._count(arr,i+1,cur_val,target)
        
        count_with = self._count(arr,i+1,cur_val | arr[i],target)
        
        
        return count_without + count_with