class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if time<n:
            return  1+time
        else:
            flag = 0
            while time>n-1:
                time = time-(n-1)
                flag +=1
            if flag%2==0:
                return time+1
            else:
                return n-time
        