class Solution:
    def resultingString(self, s: str) -> str:
        if len(s) < 2:
            return s
        if len(s) == 2 and (abs(ord(s[0])-ord(s[1])) != 1 and abs(ord(s[0])-ord(s[1]))!=25):
            return s 
        elif len(s) == 2:
            return ""
        
        stack = []
        idx = 2
        stack.append(s[0])
        stack.append(s[1])
        while idx < len(s):
            while len(stack) >= 2 and (abs(ord(stack[-1])-ord(stack[-2])) == 1 or abs(ord(stack[-1])-ord(stack[-2]))==25):
                stack.pop()
                stack.pop()
            stack.append(s[idx])
            idx += 1
        while len(stack) >= 2 and  (abs(ord(stack[-1])-ord(stack[-2])) == 1 or abs(ord(stack[-1])-ord(stack[-2]))==25):
            stack.pop()
            stack.pop()
        return "".join(stack)
