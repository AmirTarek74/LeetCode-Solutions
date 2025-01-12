class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        unlocked = []
        for i in range(len(s)):
            if locked[i] == '0':
                unlocked.append(i)
            elif s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False
        
        while stack and unlocked and stack[-1] < unlocked[-1]:
            stack.pop()
            unlocked.pop()
        
        if stack:
            return False
        return True
