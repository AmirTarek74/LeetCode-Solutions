class Solution:
    def minSwaps(self, s: str) -> int:
        
        
        if len(s)==0:
            return 0
        res = []
        unbalanced = 0
        for c in s:
            if c == '[':
                res.append(c)
            else:
                if res:
                    res.pop()
                else:
                    unbalanced +=1

        
        return (unbalanced + 1)//2
                