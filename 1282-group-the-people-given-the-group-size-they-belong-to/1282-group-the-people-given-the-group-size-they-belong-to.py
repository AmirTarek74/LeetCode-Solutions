class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = {}
        
        for i in range(len(groupSizes)):
            if groupSizes[i] not in list(d.keys()):
                d[groupSizes[i]] =[[i]]
            else:
                if len(d[groupSizes[i]][-1])==groupSizes[i]:
                    d[groupSizes[i]].append([i])
                else:
                    d[groupSizes[i]][-1].append(i)
        
        pair = [[k,v] for k,v in d.items()]
        pair.sort()
        res = []
        for p in pair:
            for v in p[1]:
                res.append(v)
        
        return res
            
        