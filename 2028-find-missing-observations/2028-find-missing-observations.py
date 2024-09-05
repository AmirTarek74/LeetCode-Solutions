class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        missing = (n+m) * mean - sum(rolls)
        if missing < n or missing/6 > n :
            return []
        res = []
        while n:
            if missing/6>=n:
                res.append(6)
                missing -=6
                n-=1
            elif missing/5>=n:
                res.append(5)
                missing -=5
                n-=1
            elif missing/4>=n:
                res.append(4)
                missing -=4
                n-=1
            elif missing/3>=n:
                res.append(3)
                missing -=3
                n-=1
            elif missing/2>=n:
                res.append(2)
                missing -=2
                n-=1
            else:
                res.append(1)
                missing -=1
                n -= 1
                
        return res
    
        