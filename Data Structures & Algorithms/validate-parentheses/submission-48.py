class Solution:
    def isValid(self, s: str) -> bool:
        closeBracket = '}])'
        openBracket = '([{'
        stack = []

        for c in s:
            if c in openBracket:
                stack.append(c)
            if c in closeBracket and not stack:
                return False
            if c == ']' and stack:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            if c == '}' and stack:
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            if c == ')' and stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
            