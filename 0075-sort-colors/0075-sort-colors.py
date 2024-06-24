class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        c = []
        
        for i in range(3):
            for _ in range(nums.count(i)):
                c.append(i)
        
        for i in range(len(nums)):
            nums[i] = c[i]
            
        