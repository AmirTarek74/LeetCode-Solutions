class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        q1 = []
        q2 = []
        for c in s:
            if c!='#':
                q1.append(c)
            else:
                if q1:
                    q1.pop()
        
        for c in t:
            if c!='#':
                q2.append(c)
            else:
                if q2:
                    q2.pop()
        
        return "".join(q1) == "".join(q2)