class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        count = [0] * 3
        n = len(s)
        
        for c in s:
            count[ord(c)-ord("a")] += 1
        
        for i in range(3):
            if count[i] < k:
                return -1
        
        window = [0] * 3
        
        l = 0 
        max_window = 0
        
        for r in range(n):
            window[ord(s[r]) - ord("a")] += 1
            while l<=r and ( (count[0]-window[0]<k) or (count[1]-window[1]<k) or (count[2]-window[2]<k) ):
                window[ord(s[l]) - ord("a")] -= 1
                l += 1
            
            max_window = max(max_window, r - l + 1)
        
        return n - max_window