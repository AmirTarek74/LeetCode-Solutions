class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        
        max_heap = [(-ord(c), cnt) for c, cnt in Counter(s).items()]
        
        heapq.heapify(max_heap)
        
        res = []
        
        while max_heap:
            ord_neg, cnt = heapq.heappop(max_heap)
            c = chr(-ord_neg)
            use = min(cnt, repeatLimit)
            res.append(c*use)
            
            if cnt > use and max_heap:
                nex_ord_neg, nex_cnt = heapq.heappop(max_heap)
                res.append(chr(-nex_ord_neg))
                if nex_cnt > 1:
                    heapq.heappush(max_heap, (nex_ord_neg, nex_cnt - 1))
                heapq.heappush(max_heap, (ord_neg, cnt - use))
        
        return "".join(res)
        