class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        res = {}
        minHeap = []
        idx = 0
        
        for q in sorted(queries):
            while idx<len(intervals) and intervals[idx][0]<=q:
                
                l,r = intervals[idx]
                heapq.heappush(minHeap,(r-l+1,r))
                idx+=1
            
            
            while minHeap and minHeap[0][1] <q :
                
                heapq.heappop(minHeap)
            
            if minHeap:
                res[q] = minHeap[0][0]
            else:
                res[q] = -1
        
        return [res[q] for q in queries]