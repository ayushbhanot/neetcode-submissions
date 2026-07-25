import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {"+" : operator.add, "-" : operator.sub, "*" : operator.mul, "/" : self.divide}
        stack = []
        for token in tokens:
            if token in operands:
                a = stack.pop()
                b = stack.pop()
                res = operands[token](b, a)
                stack.append(res)
            else:
                stack.append(int(token))

        return stack[-1]


    def divide(self, a, b):
        return int(a / b)