class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        q = []
        for c in operations:
            if c =='+':
                
                q.append(q[-1]+q[-2])
            elif c == 'D':
                
                q.append(q[-1]*2)
            elif c=='C':
                q.pop()
            else:
                q.append(int(c))
        
        
        return sum(q)