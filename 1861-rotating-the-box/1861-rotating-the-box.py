class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        
        m = len(box)
        n = len(box[0])
        
        res = [[0]* m for _ in range(n)]
        
        
        for i in range(n):
            for j in range(m):
                res[i][j] = box[m-1-j][i]
        
        for j in range(m):
            for idx in range(n-1, -1, -1):
                if res[idx][j] != ".":
                    continue
                Obstcale = False
                Stone = False
                temp = idx
                while temp != 0 :
                    if res[temp][j] == ".":
                        temp -= 1
                    elif res[temp][j] == "#":
                        Stone = True
                        break
                    else:
                        Obstcale = True
                        break
                
                if Stone:
                    res[temp][j], res[idx][j] = res[idx][j], res[temp][j]
                elif Obstcale:
                    idx = temp - 1
                elif temp == 0 and res[temp][j] == '#':
                    res[temp][j], res[idx][j] = res[idx][j], res[temp][j]
        
        return res
                    
