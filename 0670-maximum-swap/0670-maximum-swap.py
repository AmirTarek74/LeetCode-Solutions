class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = str(num)
        res = num
        
        n = len(num_str)
        for i in range(n):
            for j in range(i+1,n):
                str_lst = list(num_str)
            
                str_lst[i],str_lst[j] = str_lst[j],str_lst[i]

                res = max(res,int("".join(str_lst)))
        
        return res
                