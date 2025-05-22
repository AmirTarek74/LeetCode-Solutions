class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)

        for i in range(len(nums)):
            curr = 0
            while curr <= nums[i]:
                if (curr | (curr +1)) == nums[i]:
                    res[i] = curr
                    break
                curr += 1
        return res
