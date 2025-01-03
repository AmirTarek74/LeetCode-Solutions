class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        sufix = [0] * (n + 1)

        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + nums[i-1]
        
        for i in range(n, 0, -1):
            sufix[i-1] = sufix[i] + nums[i-1]
        
        res = 0
        for i in range(0, n-1):
            if prefix[i+1] >= sufix[i+1]:
                res += 1
        
        return res