class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operands = "-+/*"
        stack = []
        for token in tokens:
            if token in operands:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    result = a + b
                elif token == "-":
                    result = a - b
                elif token == "*":
                    result = a * b
                elif token == "/":
                    result = int(a / b)
                stack.append(result)
                continue
            stack.append(int(token))
        return stack[-1]