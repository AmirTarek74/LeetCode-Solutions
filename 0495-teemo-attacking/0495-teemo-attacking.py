class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        res = 0
        for i in range(len(timeSeries)):
            if i==0:
                res+= duration
            else:
                if timeSeries[i]>=duration+timeSeries[i-1]:
                    res+= duration
                else:
                    res-= duration
                    res = res + (timeSeries[i] - timeSeries[i-1])
                    res += duration
                    
        return res
        