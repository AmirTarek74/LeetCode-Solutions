class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        string = ""
        flag = False
        for idx in range(len(s)):
            string += s[idx]
            for j in range(idx+1,len(s),len(string)):
                if string == s[j:j+len(string)]:
                    flag = True
                else:
                    flag = False
                    break
            if flag:
                return True
        
        return False
            