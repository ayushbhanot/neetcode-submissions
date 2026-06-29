class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openBracket = '[{('


        if not s:
            return True
        
        if s[0] in '}])':
            return False

        for c in s:
            if c in openBracket:
                stack.append(c)
            if c in '}])' and not stack:
                return False
            if c in ')]}' and stack:
                if c == '}' and stack[-1] == '{':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                elif c == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            
        if len(stack) == 0:
            return True
        else:
            return False
        