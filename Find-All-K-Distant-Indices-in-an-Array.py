class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        q = []
        for i in  range(len(nums)):
            if nums[i] == key:
                q.append(i)
        res = set()
        for i in q:
            for j in range(max(0, i-k), min(i+k+1, len(nums))):
                res.add(j)
        return list(res)

        