class Solution:
    def findAnagrams(self, s2: str, s1: str) -> List[int]:
        
        
        lst = [c for c in s1]
        lst.sort()
        
        k = len(s1)
        l = 0
        res = []
        for r in range(len(s2)):
            if r-l + 1==k:
                temp = [c for c in s2[l:r+1]]
                temp.sort()
                if lst==temp:
                    res.append(l)
                l+=1
        
        return res