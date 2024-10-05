class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        possible = [-1 if x==0 else 1 for x in possible ]
        
        pre_sum = 0
        win = sum(possible)//2
        for i in range(len(possible)-1):
            pre_sum += possible[i]
            if pre_sum >win  :
                return i+1
        
        return -1
            
        