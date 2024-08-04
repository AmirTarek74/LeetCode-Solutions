class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        out = []
        for token in tokens:
            if token == '+':
                num2 = out.pop()
                num1 = out.pop()
                out.append(num1+num2)
            elif token == '-':
                num2 = out.pop()
                num1 = out.pop()
                out.append(num1-num2)
            elif token == '*':
                num2 = out.pop()
                num1 = out.pop()
                out.append(num1*num2)
            elif token == '/':
                num2 = out.pop()
                num1 = out.pop()
                out.append(int(num1/num2))
            else:
                out.append(int(token))
        return out[0]
