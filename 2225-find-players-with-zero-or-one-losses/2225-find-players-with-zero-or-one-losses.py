class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = {}
        
        for match in matches:
            d[match[0]] = d.get(match[0],0) + 0
            d[match[1]] = d.get(match[1],0) + 1
        
        pair = [(k,v) for k,v in d.items()]
        pair.sort(key=lambda x:x[1])
        
        out1 = []
        out2 = []
        for p in pair:
            if p[1]==0:
                out1.append(p[0])
            elif p[1]==1:
                out2.append(p[0])
            else:
                break
        out1.sort() 
        out2.sort()
        return [out1, out2]