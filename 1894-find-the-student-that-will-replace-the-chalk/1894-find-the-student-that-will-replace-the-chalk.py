class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        sum_chalk = 0
        
        for c in chalk:
            sum_chalk +=c
            if sum_chalk>k:
                break
        
        k = k%sum_chalk
        for i in range(len(chalk)):
            if chalk[i]>k:
                return i
            k-=chalk[i]
        
        return 0