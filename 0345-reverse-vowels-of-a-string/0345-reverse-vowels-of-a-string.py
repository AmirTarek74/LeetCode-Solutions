class Solution:
    def reverseVowels(self, s: str) -> str:
        vows = ['a','e','i','o','u']
        l, r = 0 , len(s)-1
        s2 = [c for c in s]
        while l<r:
            if s2[l].lower() not in vows:
                l+=1
                
            if s2[r].lower() not in vows:
                r-=1
            if s2[l].lower() in vows and s2[r].lower() in vows:
                s2[l],s2[r] = s2[r],s2[l]
                l+=1
                r-=1
        
        return ''.join(s2)