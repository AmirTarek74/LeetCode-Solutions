class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lst = [c for c in s1]
        lst.sort()
        
        k = len(s1)
        l = 0
        
        for r in range(len(s2)):
            if r-l + 1==k:
                temp = [c for c in s2[l:r+1]]
                temp.sort()
                if lst==temp:
                    return True
                l+=1
        
        return False