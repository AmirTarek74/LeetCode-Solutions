class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l,r = 1, max(piles)
        
        res = r
        
        while l<=r:
            
            k = (l+r)//2
            totaltime = 0
            for p in piles:
                totaltime += math.ceil(float(p)/k)
                
            if totaltime<=h:
                r = k - 1
                res = k
            elif totaltime >h:
                l = k + 1

        
        return res
                
        