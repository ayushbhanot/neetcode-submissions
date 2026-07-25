class Solution:
    def isValid(self, s: str) -> bool:
        
        closingBrackets = {"]" : "[", "}" : "{", ")" : "("}
        stack = []
        for c in s:
            if c in closingBrackets:
                if stack and  stack[-1] == closingBrackets[c]:
                    stack.pop()
                    continue
                else:
                    return False
            stack.append(c)
        return len(stack) == 0


        