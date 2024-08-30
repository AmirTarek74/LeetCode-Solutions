class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        pair = [(s,e,v) for s,e,v in zip(startTime,endTime,profit)]
        
        pair.sort()
        
        heap = []
        
        res1, res2 = 0, 0
        
        for s,e,v in pair:
            while heap and heap[0][0]<=s:
                res1 = max(res1, heapq.heappop(heap)[1])
            
            res2 = max(res2, res1+v)
            heapq.heappush(heap,(e,res1+v))
            
        return res2