class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        d = {}
        
        for bill in bills:
            if bill==5:
                d[5] = d.get(5,0) + 1
            elif bill==10:
                if d.get(5,0)>0:
                    d[5] -= 1
                    d[10] = d.get(10,0) + 1
                else:
                    return False
            else:
                
                if d.get(5,0)>0 and d.get(10,0)>0:
                    d[5] -= 1
                    d[10] -= 1
                elif d.get(5,0)>=3:
                    d[5] -= 3
                else:
                    return False
        return True
      
        return True