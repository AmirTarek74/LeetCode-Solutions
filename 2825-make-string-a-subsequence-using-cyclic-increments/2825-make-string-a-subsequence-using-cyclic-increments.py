class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        
        s2_l = 0
        l_s1, l_s2 = len(str1), len(str2)
        
        for i in range(l_s1):
            if s2_l < l_s2 and (str1[i]==str2[s2_l] or ord(str1[i]) + 1 == ord(str2[s2_l]) or ord(str1[i]) + 1 == ord(str2[s2_l]) + 26):
                
                s2_l += 1
            
        return l_s2 == s2_l
        