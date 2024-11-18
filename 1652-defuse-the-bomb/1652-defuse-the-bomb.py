class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n
        if k == 0 :
            return res
        for i in range(n):
           
            if k>0:
                temp = 0
                for j in range(k):
                    temp += code[(i+1+j)%n]
                res[i] = temp
            else:
                temp = 0
                for j in range(-k):
                    temp += code[(i-1-j)%n]
                res[i] = temp
        
        return res
        