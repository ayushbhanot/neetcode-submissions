class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openBracket = '([{'
        closeBracket = '})]'

        for i in range(len(s)):
            if s[0] in closeBracket:
                return False
    
        for c in s:
            if c in openBracket:
                stack.append(c)

            if c in closeBracket:
                if not stack:
                    return False
                if c == '}' and stack[-1] == '{':
                    stack.pop()
                elif c == ')' and stack[-1] == '(':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False