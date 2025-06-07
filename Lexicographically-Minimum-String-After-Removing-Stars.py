class Solution:
    def clearStars(self, s: str) -> str:
        if "*" not in s:
            return s
        
        heap = []
        res = [c for c in s]
        for i in range(len(s)):
            if s[i] == "*" and heap:
                _, idx  = heapq.heappop(heap)
                res[-idx] = ""
                res[i] = ""
            else:
                heapq.heappush(heap, (s[i], -i))
        
        return "".join(res)