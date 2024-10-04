class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill.sort()
        pairs = []
        l = 0
        r = len(skill)-1
        while l<r:
            pairs.append([skill[l],skill[r]])
            l +=1
            r -=1
        
        prev_sum = sum(pairs[0])
        res = 0
        for p in pairs:
            if prev_sum != sum(p):
                return -1
            else:
                res = res + p[0]*p[1]
        
        return res
                
        
        
        