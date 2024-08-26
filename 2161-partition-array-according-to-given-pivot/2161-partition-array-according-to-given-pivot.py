class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left=[]
        right=[]
        i = 0
        while i<len(nums):
            if nums[i]<pivot:
                left.append(nums.pop(i))
            elif nums[i]>pivot:
                right.append(nums.pop(i))
            else:
                i+=1
        
        return left + nums + right
        