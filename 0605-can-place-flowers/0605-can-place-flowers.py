class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        last = float("-inf")
        
        for i in range(len(flowerbed)):
            if n==0:
                return True
            if flowerbed[i]==0 :
                l = (i==0) or (flowerbed[i-1]==0)
                r = (i==len(flowerbed)-1) or (flowerbed[i+1]==0)     
                if l and r:
                    n-=1
                    flowerbed[i] = 1
            
        if n==0:
            return True
        else:
            return False
                
        