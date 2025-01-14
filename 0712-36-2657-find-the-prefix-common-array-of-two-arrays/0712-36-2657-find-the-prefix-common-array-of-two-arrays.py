class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        c = [0] * len(A)
        if A[0]==B[0]:
            c[0] = 1
            
        for i in range(1,len(A)):
            if A[i]==B[i]:
                c[i] += c[i-1] + 1
            else:
                count = 0
                if A[i] in B[0:i]:
                    count +=1
                if B[i] in A[0:i]:
                    count+=1
                c[i] += c[i-1]+count
        
        return c