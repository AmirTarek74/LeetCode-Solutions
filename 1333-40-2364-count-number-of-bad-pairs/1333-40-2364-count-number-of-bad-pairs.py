class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        good_pairs_map = {}
        res = 0

        for j in range(len(nums)):
            diff = j - nums[j]
            good_pairs = good_pairs_map.get(diff,0)
            res = res + j - good_pairs
            good_pairs_map[diff] = good_pairs + 1
        return res