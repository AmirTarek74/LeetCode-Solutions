class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        l = 1
        r = x
        while l<=r:
            mid = (l+r)//2
            if mid*mid==x:
                return mid
            elif mid*mid>x:
                r = mid - 1
            else:
                l = mid + 1
        
        return floor(r)
        