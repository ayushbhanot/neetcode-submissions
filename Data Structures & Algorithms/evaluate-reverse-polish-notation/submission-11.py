class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = "+-*/"

        while len(tokens) > 1:
            for i in range(len(tokens)):
                if tokens[i] in operators:
                    a = int(tokens[i - 2])
                    b = int(tokens[i - 1])
                    if tokens[i] == "+":
                        tokens[i] = a + b
                    elif tokens[i] == "-":
                        tokens[i] = a - b
                    elif tokens[i] == "*":
                        tokens[i] = a * b
                    elif tokens[i] == "/":
                        tokens[i] = int(a / b)
                    tokens = tokens[:i - 2] + [str(tokens[i])] + tokens[i + 1:]
                    break
        return int(tokens[0])