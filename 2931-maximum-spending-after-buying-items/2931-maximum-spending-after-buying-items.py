class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        m,n = len(values), len(values[0])
        ans = []
        for i in range(m):
            for j in range(n):
                ans.append(values[i][j])
        ans.sort()
        d = 1
        res = 0
        for i in range(len(ans)):
            res = res + ans[i]*d
            d +=1
            
        
        return res
            