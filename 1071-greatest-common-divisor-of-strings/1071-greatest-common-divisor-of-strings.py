class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1,l2 = len(str1), len(str2)
        def check(k):
            if l1%k or l2%k:
                return False
            
            n1 = l1 // k
            n2 = l2 // k
            base = str1[:k]
            
            return str1 == base * n1 and str2 == base * n2
        
        for i in range(min(l1,l2),0,-1):
            if check(i):
                return str1[:i]
        
        return ""