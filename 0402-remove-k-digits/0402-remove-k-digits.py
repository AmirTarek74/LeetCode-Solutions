class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num) or k>len(num):
            return '0'
        
        res = ''
        
        q = []
        for n in num:
            while q and k>0 and q[-1]>n:
                q.pop()
                k-=1
            q.append(n)
        
        q = q[:-k] if k>0 else q
        
        res = ''.join(q).lstrip('0')
        
        return res if res else '0'