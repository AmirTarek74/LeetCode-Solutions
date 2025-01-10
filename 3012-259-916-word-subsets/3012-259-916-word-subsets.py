class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count(word):
            ans = [0] * 26
            for c in word:
                ans[ord(c)-ord("a")] += 1

            return ans
        
        bmax = [0] * 26
        for b in words2:
            for i,c in enumerate(count(b)):
                bmax[i] = max(bmax[i], c)
        
        res = []
        for a in words1:
            if all(x>=y for x,y in zip(count(a), bmax)):
                res.append(a)
        
        return res
               