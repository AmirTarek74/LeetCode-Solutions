class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        
        for q in queries:
            c = 0
            for p in points:
                
                if ((q[0]-p[0])**2 + (q[1]-p[1])**2)**0.5<=q[2]:
                    
                    c+=1
            
            res.append(c)
        
        return res
                
        