class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        pair = [(a,b) for a,b in zip(aliceValues,bobValues)]
        
        pair.sort(key = lambda x: sum(x), reverse = True)
        
        aliceChose= True
        a = 0
        b = 0
        for p in pair:
            if aliceChose:
                a+= p[0]
                aliceChose = False
            else:
                b += p[1]
                aliceChose = True
        
        if a>b:
            return 1
        elif a<b:
            return -1
        else:
            return 0
        