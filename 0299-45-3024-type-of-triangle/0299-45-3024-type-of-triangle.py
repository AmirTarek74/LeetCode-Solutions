class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[2] >= nums[0] + nums[1]:
            return "none"
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        for k in d:
            if d[k]==3:
                return "equilateral"
            
            if d[k] == 2:
                return "isosceles"
        return "scalene"