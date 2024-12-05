class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if 0 in [num1, num2]:
            return "0"
        
        res = []
        count = 0
        for i in range(len(num2)-1, -1 , -1):
            temp = 0
            rem = 0
            idx = 0
            for j in range(len(num1)-1, -1 , -1):
                digit = int(num2[i]) * int(num1[j]) + rem
                rem = digit // 10
                temp  =  (digit % 10) * 10**(idx) + temp
                idx += 1
            if rem != 0:
                temp = rem* 10**len(num1) + temp
            temp = temp * 10**count
            count += 1
            res.append(temp)
        final = sum(res)
        return str(final)
            