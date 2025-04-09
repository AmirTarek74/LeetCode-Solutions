class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = set()
        for x in nums:
            if x > k :
                res.add(x)
            elif x < k:
                return -1
        return len(res)
