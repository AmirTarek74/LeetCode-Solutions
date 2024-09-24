class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l,r = 1, totalTrips*min(time)
        
        def f(x):
            return sum(x//t for t in time)>=totalTrips
        
        while l<r:
            mid = (l+r)//2
            if not(f(mid)):
                l = mid + 1
            else:
                r = mid
        return l
        
        return t-1
            
        