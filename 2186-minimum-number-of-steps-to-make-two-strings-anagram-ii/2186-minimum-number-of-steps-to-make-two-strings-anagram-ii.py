from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        d1 = dict(Counter(s))
        d2 = dict(Counter(t))
        
        
        res = 0
        for k in 'abcdefghijklmnopqrstuvwxyz':
            res =  res + abs(d1.get(k,0)-d2.get(k,0))
        
        return res