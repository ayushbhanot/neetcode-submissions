class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '[' or c == '(' or c == '{':
                stack.append(c)
            if c == ']' or c == ')' or c == '}':
                if not stack:
                    return False
                if (c == ']' and stack[-1] != '[') or (c == '}' and stack[-1] != '{') or (c == ')' and stack[-1] != '('):
                    return False
                else:
                    stack.pop()
            
        if len(stack) == 0:
            return True
        else:
            return False