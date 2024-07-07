class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts.sort(reverse=True)
        
        for _ in range(k):
            item = gifts.pop(0)
            gifts.append(int(sqrt(item)))
            gifts.sort(reverse=True)
        
        return sum(gifts)
            
        