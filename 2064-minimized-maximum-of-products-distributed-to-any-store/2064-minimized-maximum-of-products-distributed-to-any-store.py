class Solution:
    def canDistribute(self, x, q, n):
        j = 0
        rem = q[0]
        
        for i in range(n):
            if rem<=x:
                j += 1
                if j == len(q):
                    return True
                else:
                    rem = q[j]
            else:
                rem = rem - x
        return False
    
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l = 0
        r = max(quantities)
        
        while l< r :
            mid = (l + r )//2
            if self.canDistribute(mid, quantities, n):
                r = mid 
            else:
                l = mid + 1
        
        return l