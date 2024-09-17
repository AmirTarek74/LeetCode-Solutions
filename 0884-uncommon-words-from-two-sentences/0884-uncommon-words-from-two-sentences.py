class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        d1 = dict(collections.Counter(s1.split(' ')))
        d2 = dict(collections.Counter(s2.split(' ')))
        res = set()
        for k in d1:
            if d1[k]==1 and d2.get(k,0)==0:
                res.add(k)
        
        for k in d2:
            if d2[k]==1 and d1.get(k,0)==0:
                res.add(k)
        
        return list(res)