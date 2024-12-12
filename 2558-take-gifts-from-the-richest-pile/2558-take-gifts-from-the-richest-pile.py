class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gift_h = [-g for g in gifts]
        heapq.heapify(gift_h)
        
        for _ in range(k):
            gift = - heapq.heappop(gift_h)
            
            heapq.heappush(gift_h, - int(math.sqrt(gift)))
        
        res = 0
        while gift_h:
            
            res = res - heapq.heappop(gift_h)
        
        return res
        