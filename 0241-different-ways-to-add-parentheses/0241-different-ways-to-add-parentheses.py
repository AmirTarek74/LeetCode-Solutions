class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        if len(expression) == 0:
            return res
        elif len(expression)== 1:
            res.append(int(expression[0]))
            return res
        elif len(expression) == 2 and expression[0].isdigit():
            res.append(int(expression[:]))
            return res
        
        for i,c in enumerate(expression):
            if c.isdigit():
                continue
            
            left_res = self.diffWaysToCompute(expression[:i])
            right_res = self.diffWaysToCompute(expression[i+1:])
            for left in left_res:
                for right in right_res:
                    if c == '+':
                        res.append(left+right)
                    elif c== '-':
                        res.append(left-right)
                    elif c=='*':
                        res.append(left*right)
        
        return res
            