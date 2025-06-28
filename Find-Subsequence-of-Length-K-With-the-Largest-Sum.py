class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i], i))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        while heap:
            res.append(heapq.heappop(heap))
        res.sort(key=lambda x:x[1])
        return [c for c,i in res]