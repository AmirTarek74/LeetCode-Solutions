class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c=='(' or c=='[' or c=='{':
                stack.append(c)
            elif c==')':
                if len(stack)==0:
                    return False
                elif stack[-1]!='(':
                    return False
                temp = stack.pop(-1)
            elif c==']':
                if len(stack)==0:
                    return False
                elif stack[-1]!='[':
                    return False
                temp = stack.pop(-1)
            elif c=='}':
                if len(stack)==0:
                    return False
                elif stack[-1]!='{':
                    return False
                temp = stack.pop(-1)
                
        
        if len(stack)==0:
            return True
        else:
            return False
        