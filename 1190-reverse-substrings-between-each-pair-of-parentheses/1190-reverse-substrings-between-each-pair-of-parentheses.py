class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = deque()
        out = []
        for c in s:
            if c=='(':
                stack.append(len(out))
            elif c==')':
                start = stack.pop()
                out[start:] = out[start:][::-1]
            else:
                out.append(c)
        return "".join(out)
        