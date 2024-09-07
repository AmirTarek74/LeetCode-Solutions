class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
    
        diff = (sum(A) - sum(B)) / 2 
        
        A = set(A)
        for b in set(B):
            if diff + b in A:
                return [diff+b , b]
            
        
        