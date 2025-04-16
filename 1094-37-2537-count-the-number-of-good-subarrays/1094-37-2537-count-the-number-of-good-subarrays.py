class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        res = 0
        d = {}
        same, r = 0, -1
        n = len(nums)

        for l in range(n):
            while same < k and r + 1 < n:
                r += 1
                same += d.get(nums[r], 0)
                d[nums[r]] = d.get(nums[r], 0 )+ 1
            if same >= k :
                res += n - r
            d[nums[l]] -= 1
            same -= d[nums[l]]
        return res