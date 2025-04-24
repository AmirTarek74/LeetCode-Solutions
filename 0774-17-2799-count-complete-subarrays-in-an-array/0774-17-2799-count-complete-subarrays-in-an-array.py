class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        
        unique = len(d)
        res = 0
        for i in range(len(nums)):
            s = set()
            for j in range(i, len(nums)):
                s.add(nums[j])
                if len(s)==unique:
                    res += 1
        
        return res