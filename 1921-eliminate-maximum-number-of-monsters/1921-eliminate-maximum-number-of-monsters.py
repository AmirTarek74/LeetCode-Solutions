class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        
        arrival = []
        for i in range(len(dist)):
            arrival.append(dist[i]/speed[i])
        
        arrival.sort()
        res = 0
        for i in range(len(arrival)):
            if arrival[i] <= i:
                return res
            res+=1
        
        return res
                    
                    
            
            
            