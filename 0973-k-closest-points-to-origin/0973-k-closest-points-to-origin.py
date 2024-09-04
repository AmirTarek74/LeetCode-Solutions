class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pair = []
        for idx,p in enumerate(points):
            pair.append([p[0]**2 + p[1]**2, idx])
        pair.sort(key= lambda x: x[0], reverse = False)
        
        res = []
        for i in range(k):
            res.append(points[pair[i][1]])
        
        return res