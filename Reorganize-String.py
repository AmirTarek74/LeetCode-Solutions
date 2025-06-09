class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = []
        for k in count:
            heapq.heappush(heap, (-count[k], k))
        res = ""
        while len(heap) >= 2:
            if res and res[-1] == heap[0][1]:
                return ""
            cnt1, c1 = heapq.heappop(heap)
            cnt2, c2 = heapq.heappop(heap)
            res += c1 + c2
            cnt1 += 1
            cnt2 += 1
            if cnt1 != 0:
                heapq.heappush(heap, ( cnt1, c1))
            if cnt2 != 0:
                heapq.heappush(heap, ( cnt2, c2))
        if heap:
            if heap[0][0] != -1:
                return ""
            res += heap[0][1]
        return res