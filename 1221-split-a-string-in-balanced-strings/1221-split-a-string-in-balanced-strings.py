class Solution:
    def balancedStringSplit(self, s: str) -> int:
        start = 0
        idx = 1
        counter = 0
        while(idx<len(s)):
            temp = s[start:idx+1]
            if temp.count("R")==temp.count("L"):
                start = idx+1
                idx = start + 1
                counter +=1
            else:
                idx+=1
        
        return counter 