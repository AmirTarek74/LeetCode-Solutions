class Solution:
    def countLargestGroup(self, n: int) -> int:
        d1 = {}
        d2 = {}
        for i in range(1,n+1):
            temp_sum = self.digit_sum(i)
            if temp_sum not in d1:
                d1[temp_sum] = [i]
            else:
                d1[temp_sum].append(i)
        res = 0
        for k in d1:
            l = len(d1[k])
            d2[l] = d2.get(l, 0) + 1
            res = max(res, l)
        
        return d2[res]
            


    def digit_sum(self, num):
        summa = 0
        while num != 0:
            summa += num%10
            num = num//10
        return summa