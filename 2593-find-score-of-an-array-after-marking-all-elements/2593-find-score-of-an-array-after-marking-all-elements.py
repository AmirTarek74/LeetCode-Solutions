class Solution:
    def findScore(self, nums: List[int]) -> int:
        q = []
        
        for i in range(len(nums)):
            heapq.heappush(q, (nums[i], i))
        
        heapq.heapify(q)
        seen = set()
        res = 0
        
        while q:
            item, idx = heapq.heappop(q)
            if idx in seen:
                continue
            res += item
            seen.add(idx)
            if idx>0:
                seen.add(idx-1)
            if idx<len(nums)-1:
                seen.add(idx+1)
        
        return res