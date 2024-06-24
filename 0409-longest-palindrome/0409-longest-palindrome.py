class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        flag = 0 
        l = 0
        for c in s:
            if c not in list(d.keys()):
                d[c] = s.count(c)
        d = dict(sorted(d.items(), key=lambda x:x[1],reverse=True))
        for k in list(d.keys()):
            if d[k]%2==0:
                l+=d[k]
            elif d[k]%2!=0 and flag==0:
                l+=d[k]
                flag=1
            
            elif d[k]==1 and flag==0:
                l+=1
                flag = 1
            else:
                l = l+d[k]-1
        return l

        

        