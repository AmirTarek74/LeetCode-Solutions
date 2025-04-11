class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0

        for i in range(low, high+1):
            s = str(i)
            l = len(s)
            if l%2 == 1:
                continue 
            s1 = sum([int(n) for n in s[:l//2]])
            s2 = sum([int(n) for n in s[l//2:]])
            if s1 == s2:
                res += 1
        
        return res

