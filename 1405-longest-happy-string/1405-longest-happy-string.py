class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        if a > 0:
            heapq.heappush(pq, (-a, "a"))

        if b > 0:
            heapq.heappush(pq, (-b, "b"))

        if c > 0:
            heapq.heappush(pq, (-c, "c"))
            
        res = ""
        while pq:
            count, ch = heapq.heappop(pq)
            
            count = -count
            if len(res)>=2 and res[-1]==res[-2] and res[-1]==ch:
                if not pq:
                    break
                temp_ct, temp_ch = heapq.heappop(pq)
                res += temp_ch
                if (temp_ct + 1)<0:
                    heapq.heappush(pq,(temp_ct +1, temp_ch))
                heapq.heappush(pq,(-count, ch))
            else:
                res += ch
                count -= 1
                if count>0:
                    heapq.heappush(pq,(-count, ch))
        return res