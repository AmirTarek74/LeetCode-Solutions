class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        zero_counts = nums.count(0)
        l = 0
        r = len(nums) - 1
        neg = 0
        while l<=r:
            mid = (l+r)//2
            if nums[mid] < 0:
                l = mid + 1
            else:
                r = mid - 1
                neg = mid
        return max(neg, len(nums) - neg - zero_counts)
                