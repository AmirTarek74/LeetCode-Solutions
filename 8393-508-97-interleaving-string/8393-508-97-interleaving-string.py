class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n , l = len(s1), len(s2), len(s3)

        if m+n != l:
            return False
        
        memo = {}
        
        def helper(i, j, k):
            if k == l:
                return True
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            res= False
            if i <m and s1[i]==s3[k]:
                res = res or helper(i+1, j,k+1)
            
            if j<n and s2[j] == s3[k]:
                res = res or helper(i, j+1, k+1)
            
            memo[(i,j)] = res
            return res
        
        return helper(0,0,0)