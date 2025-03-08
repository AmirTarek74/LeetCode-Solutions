class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        if "B"*k in blocks:
            return 0
        
        changes = 0
        res = float("inf")
        l = 0 
        
        for r in range(len(blocks)):
            
            if blocks[r]=='W':
                changes += 1
            
            if r - l +1 == k:
                res = min(res, changes)
                if blocks[l] == 'W':
                    changes -= 1
                l += 1
    
        return res
