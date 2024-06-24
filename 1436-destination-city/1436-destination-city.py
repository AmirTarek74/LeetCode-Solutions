class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        if len(paths)==1:
            return paths[0][1]
        start = paths[0][0]
        idx = 0
        while(idx<len(paths)):
            for i in range(len(paths)):
                if paths[i][0]==start:
                    start = paths[i][1]
                    break
            idx+=1
        
        return start
        