class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        
        res = 0
        q = []
        
        for n in nums:
            heapq.heappush(q,-n)
        
        for i in range(k):
            if q:
                val = -heapq.heappop(q)
                res += val
                heapq.heappush(q,-ceil(val/3))
        
        return res