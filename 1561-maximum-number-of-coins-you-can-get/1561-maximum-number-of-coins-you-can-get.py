class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        l = 0
        
        
        res = 0
        for _ in range(len(piles)//3):
            res += piles[l+1]
            l+=2
        
        return res