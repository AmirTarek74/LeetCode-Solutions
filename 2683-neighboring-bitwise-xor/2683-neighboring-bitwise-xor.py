class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len (derived)
        
        for first in [0,1]:
            original = first
            for i in range(n-1):
                original = original ^ derived[i]
            
            if original^first == derived[-1]:
                return True
        
        
        return False
       