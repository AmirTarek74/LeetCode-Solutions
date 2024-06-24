class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2**31
        MAX = 2**31 - 1
        if x>=0:
            sign = 1
        else:
            sign = -1   
        num=0
        #x = abs(x) 
        if x%10==0:
            x= x/10
        while(x!=0):  
            digit = int(math.fmod(x,10))

            x = int(x/10)
            if (num> MAX//10 or (num == MAX//10 and digit >= MAX%10))   :
                return 0
            if (num< MIN//10 or (num == MIN//10 and digit <= MIN%10)):
                return 0
            num = num*10 + digit
            

        return num 

