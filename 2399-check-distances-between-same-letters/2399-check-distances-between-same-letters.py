class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        
        idx = {}
        for i in range(len(s)):
            if s[i] not in idx:
                idx[s[i]] = [i]
            else:
                idx[s[i]].append(i)
        
        
        for c in idx:
            d = idx[c][1] - idx[c][0]
            
            if d != distance[ord(c) - ord("a")]+1:
                return False
        
        return True