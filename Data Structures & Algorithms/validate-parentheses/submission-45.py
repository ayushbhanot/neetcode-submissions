class Solution:
    def isValid(self, s: str) -> bool:
        openBracket, closeBracket = '{[(', '}])'

        if s[0] in closeBracket:
            return False
        
        stack = []
        
        for i in range(len(s)):
            if s[i] in openBracket:
                stack.append(s[i])
            
            if s[i] in closeBracket:
                if stack:
                    if s[i] == ')' and stack[-1] == '(':
                        stack.pop()
                    elif s[i] == ']' and stack[-1] == '[':
                        stack.pop()
                    elif s[i] == '}' and stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            
        if len(stack) == 0:
            return True
        else:
            return False
