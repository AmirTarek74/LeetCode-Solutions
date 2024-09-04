class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        
        i, j = 0,0
        move = [(0,1),(1,0),(0,-1),(-1,0)]
        direction = 0
        mx = 0
        obstacles = set(map(tuple,obstacles))
        for c in commands:
            if c == -1 :
                direction = (direction+1)%4
            elif c == -2 :
                direction = (direction-1)%4
            else:
                x,y = move[direction]
                while c and (i+x,j+y) not in obstacles:
                    i += x
                    j += y
                    c -= 1
                
                    
            mx = max(mx , i**2 + j**2)
        return mx
                        
                        
