class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len (derived)
        original1 = [1] 
        original2 = [0]
        
        for i in range(1,n):
            if i==n-1:
                original1.append(original1[0] ^ derived[i])
                original2.append(original2[0] ^ derived[i])
            else:
                original1.append(original1[i-1] ^ derived[i-1])
                original2.append(original2[i-1] ^ derived[i-1])
        
        flag1 = True
        
        for i in range(n):
            if i == n-1:
                if derived[i] != original1[i] ^ original1[0]:
                    flag1 = False
                    break
            else:
                if derived[i] != original1[i+1] ^ original1[i]:
                    flag1 = False
                    break
        flag2 = True
        
        for i in range(n):
            if i == n-1:
                if derived[i] != original2[i] ^ original2[0]:
                    flag2 = False
                    break
            else:
                if derived[i] != original2[i+1] ^ original2[i]:
                    flag2 = False
                    break
        
        return flag1 or flag2
        