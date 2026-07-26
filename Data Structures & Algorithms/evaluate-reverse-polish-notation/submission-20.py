class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = "+-/*"

        def dfs():
            popped = tokens.pop()
            if popped in operands:
                right = dfs()
                left = dfs()

                if popped == "+":
                    return left + right
                elif popped == "-":
                    return left - right
                elif popped == "*":
                    return left * right
                elif popped == "/":
                    return int(left / right)
            else:
                return int(popped)
        return dfs()