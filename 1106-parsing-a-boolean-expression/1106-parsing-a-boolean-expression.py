class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        
        st = deque()
        
        for c in expression:
            if c == ')':
                values = []
                
                while st[-1] !='(':
                    values.append(st.pop())
                st.pop()
                op = st.pop()
                
                res = self._subexp(op,values)
                st.append(res)            
            
            elif c != ',':
                st.append(c)
                
        return st[-1]=='t'
    
    def _subexp(self,op,values):
        
        if op=='!':
            return "f" if values[0]=='t' else 't'
        
        if op == '&':
            for val in values:
                if val == 'f':
                    return 'f'
            return 't'
        
        if op == '|':
            for val in values:
                if val == 't':
                    return 't'
            return 'f'
        return 'f'