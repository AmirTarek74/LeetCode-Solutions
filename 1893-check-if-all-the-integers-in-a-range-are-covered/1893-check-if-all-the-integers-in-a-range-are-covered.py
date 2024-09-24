class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
       
        
        for i in range(left,right+1):
            found = False
            for rng in ranges:
                if  (rng[0]<=i<=rng[1]):
                    found = True
                    break
            if not found:
                return False
            
        return True