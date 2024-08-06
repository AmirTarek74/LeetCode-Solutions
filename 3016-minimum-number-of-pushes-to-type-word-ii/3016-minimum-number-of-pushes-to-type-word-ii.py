class Solution:
    def minimumPushes(self, word: str) -> int:
        min_pushes = 0
        
        frequencey = [0] * 26
        
        for c in word:
            frequencey[ord(c) - ord("a")] += 1
        
        frequencey.sort(reverse=True)
        
        for i in range(26):
            if frequencey[i]==0:
                break
            
            min_pushes += (i//8 + 1) * frequencey[i]
            
        return min_pushes    
        
        