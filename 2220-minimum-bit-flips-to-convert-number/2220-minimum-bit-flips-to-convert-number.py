class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        s1 = ''
        s2 = ''
        
        while start:
            s1 += '0' if start%2==0 else '1' 
            start = start//2
        
        while goal:
            s2 += '0' if goal%2==0 else '1' 
            goal = goal//2
        while len(s1)<len(s2):
            s1 += '0'
        while len(s2)<len(s1):
            s2 += '0'
        
        c = 0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                c+=1
        
        return c
            
        