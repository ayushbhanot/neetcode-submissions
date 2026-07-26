class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operands = "-+/*"

        while len(tokens) > 1:
            for i in range(len(tokens)):
                if tokens[i] in operands:
                    a = int(tokens[i - 2])
                    b = int(tokens[i - 1])
                    if tokens[i] == "+":
                        result = a + b
                    elif tokens[i] == "-":
                        result = a - b
                    elif tokens[i] == "*":
                        result = a * b
                    elif tokens[i] == "/":
                        result = int(a / b)
                    tokens = tokens[: i - 2] + [str(result)] + tokens[i + 1 :]
                    break
        return int(tokens[0]) #O(n2) time and O(n) space