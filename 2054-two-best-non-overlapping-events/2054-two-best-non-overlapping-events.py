class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        events.sort()
        
        heap = []
        res1,res2 = 0,0
        
        for s,e,v in events:
            
            while heap and heap[0][0]<s:
                res1 = max(res1, heapq.heappop(heap)[1])
                
            res2 = max(res2, res1 +v)
            heapq.heappush(heap,(e,v))
        
        return res2
        