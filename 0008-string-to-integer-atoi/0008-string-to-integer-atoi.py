class Solution:
    def myAtoi(self, s: str) -> int:
        is_negative = False
        started = False
        res = 0
        for c in s:
            if c==' ':
                if started:
                    break
                continue
            elif c=='-':
                if started:
                    break
                is_negative = True
                started = True
            elif c=='+':
                if started:
                    break
                started = True
            elif not c.isdigit():
                break
            else:
                started = True
                res = res *10+int(c)
        if is_negative:
            if res>2**31:
                res = 2**31
        else:
            if res>2**31 - 1:
                res = 2**31 - 1
        
        if is_negative:
            return -1*res
        else:
            return res
        