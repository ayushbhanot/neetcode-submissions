class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        closeToOpen = {']' : '[', '}' : '{', ')' : '('}
        for c in s: #O(s) time
            
            if c in closeToOpen and stack:
                if stack[-1] == closeToOpen[c]:
                    stack.pop()
                    continue
            stack.append(c)

        if len(stack) == 0:
            return True
        else:
            return False