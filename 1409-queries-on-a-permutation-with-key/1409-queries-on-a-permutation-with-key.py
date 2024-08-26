class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        
        res = []
        p = list(range(1,m+1))
        for q in queries:
            idx = p.index(q)
            res.append(idx)
            p.insert(0,p.pop(idx))
        
        return res
        