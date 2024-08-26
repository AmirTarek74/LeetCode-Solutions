class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        d = {"G":0,"M":0,"P":0}
        travel.insert(0,0)
        
        res = 0
        
        for i in range(len(garbage)):
            for c in set(garbage[i]):
                res = res + sum(travel[d[c]:i+1]) - travel[d[c]] + garbage[i].count(c)
                d[c] = i
        
        return res
            
            
        