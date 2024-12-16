class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        min_heap = []
        for i in range(len(nums)):
            heapq.heappush(min_heap,(nums[i], i))
        
        for _ in range(k):
            item, i = heapq.heappop(min_heap)
            heapq.heappush(min_heap,(item * multiplier , i))
        
        res = [-1] * len(nums)
        while min_heap:
            item, i = heapq.heappop(min_heap)
            res[i] = item
        
        return res