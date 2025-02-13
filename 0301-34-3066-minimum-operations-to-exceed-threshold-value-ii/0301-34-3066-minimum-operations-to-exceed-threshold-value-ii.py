class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        q = []
        heapq.heapify(q)
        for n in nums:
            heapq.heappush(q, n)
        

        res = 0
        while len(q)>=2:
            if q[0]>=k:
                return res
            n1 = heapq.heappop(q)
            n2 = heapq.heappop(q)
            temp = min(n1,n2)*2+max(n1,n2)
            heapq.heappush(q, temp)
            res += 1
        
        return res