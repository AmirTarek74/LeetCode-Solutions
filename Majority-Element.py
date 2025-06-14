class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        holding = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == holding:
                count += 1
            else:
                count -= 1
                if count == 0:
                    holding = nums[i]
                    count = 1
        return holding