class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        happy = 0
        g.sort(reverse=False)
        s.sort(reverse=False)
        temp=-1
        i = 0
        while(i<len(g) and i<len(s)):
            for c in range(temp+1,len(s)):
                if g[i]<=s[c]:
                    happy+=1
                    temp = c
                    break

            i+=1
        
        return happy
        