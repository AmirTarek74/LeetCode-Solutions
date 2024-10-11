class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        target = times[targetFriend]
        times.sort()
        
        max_time = max([max(i) for i in times])
        
        t = times[0][0]
        
        q = []
        heapq.heapify(q)
        i = 0
        empty = [0]
        heapq.heapify(empty)
        while i<len(times) and t<max_time:
            
            while q and q[0][0]==t:
                heapq.heappush(empty,q[0][2])
                heapq.heappop(q)
            
            if t==target[0]:
                return empty[0]
            
            if t==times[i][0]:
                heapq.heappush(q,[times[i][1],times[i][0],empty[0]])
                if len(empty)==1:
                    heapq.heappush(empty,empty[0]+1)
                    heapq.heappop(empty)
                else:
                    heapq.heappop(empty)
                i+=1
                
            t +=1
            
            
        