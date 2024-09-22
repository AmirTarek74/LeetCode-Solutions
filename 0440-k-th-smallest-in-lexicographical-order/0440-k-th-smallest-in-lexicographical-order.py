class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        
        curr = 1
        k -=1
        while k>0:
            temp = self.countSteps(n,curr,curr+1)
            if temp<=k:
                curr +=1
                k -= temp
            else:
                curr *= 10
                k -=1
        return curr

    def countSteps(self,n,curr,curr2):
        steps = 0
        while curr<=n:
            steps = steps + min(n+1,curr2) - curr
            curr *=10
            curr2 *=10
        
        return steps
                
        