
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for word in words:
            d[word] = d.get(word,0) + 1
        max_heap = []
        for key in d:
            heapq.heappush(max_heap, (-d[key], key))
        res = []
        for _ in range(k):
            _, word = heapq.heappop(max_heap)
            res.append(word)
        
        return res
            
        