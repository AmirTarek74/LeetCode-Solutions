class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = [-i for i in stones]
        heapq.heapify(q)
        while len(q)>1:
            n1 = -heapq.heappop(q)
            n2 = -heapq.heappop(q)
            if n1!=n2:
                temp = max(n1,n2)-min(n1,n2)
                heapq.heappush(q,-temp)
        
        if q:
            return -q[0]
        else:
            return 0