class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        idx = 0
        lst = list(range(1,n+1))
        while(len(lst)>1):
            idx = idx + k - 1
            if idx>len(lst)-1:
                idx = idx%len(lst)
            temp = lst.pop(idx)
            
            #idx = (idx+1)
           # if idx> len(lst)-1:
              #  idx = idx%len(lst)
        return lst[0]
        
        