class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        n = len(nums)
        idx_stack = []
        res = 0
        
        for i in range(n):
            if not idx_stack or nums[idx_stack[-1]]>nums[i]:
                idx_stack.append(i)
        
        
        for j in range(n-1,-1,-1):
            while idx_stack and nums[idx_stack[-1]]<= nums[j]:
                res = max(res, j - idx_stack[-1])
                idx_stack.pop()
                
        return res
        