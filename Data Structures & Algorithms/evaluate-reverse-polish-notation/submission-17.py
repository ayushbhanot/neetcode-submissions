class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = "+-/*"

        for i in range(len(tokens)): #O(n) time
            if tokens[i] in operands:
                b = stack.pop()
                a = stack.pop()
                if tokens[i] == "+":
                    result = a + b
                elif tokens[i] == "-":
                    result = a - b
                elif tokens[i] == "*":
                    result = a * b
                elif tokens[i] == "/":
                    result = int(a / b)
                stack.append(result)
                continue
            stack.append(int(tokens[i]))

        return stack[-1]