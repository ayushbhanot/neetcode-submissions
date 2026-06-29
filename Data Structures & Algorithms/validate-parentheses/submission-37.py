class Solution:
    def isValid(self, s: str) -> bool:
        openBracket, closeBracket = '({[', ']})'
        stack = []

        if s[0] in closeBracket:
            return False

        for c in s:
            if c in openBracket:
                stack.append(c)

            if c in closeBracket:
                if stack:
                    if c == '}' and stack[-1] == '{':
                        stack.pop()
                    elif c == ']' and stack[-1] == '[':
                        stack.pop()
                    elif c == ')' and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False