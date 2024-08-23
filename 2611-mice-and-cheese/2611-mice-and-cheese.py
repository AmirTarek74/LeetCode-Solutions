class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        
        diff = [[]] * len(reward1)
        
        for i in range(len(reward1)):
            diff[i] = [reward2[i]-reward1[i],i]
        
        diff.sort()
        
        res = 0
        seen =[False] * len(reward1)
        for i in range(k):
            idx = diff[i][1]
            res += reward1[idx]
            seen[idx] = True
        
        for i in range(len(reward1)):
            if seen[i] == True:
                continue
            
            res += reward2[i]
        
        return res
                           
                           
                           
                           