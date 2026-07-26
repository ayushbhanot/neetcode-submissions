class DoublyLinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = "-+/*"

        curr = DoublyLinkedList(int(tokens[0]))

        for i in range(1, len(tokens)): #O(n) time
            if tokens[i] in operands:
                a = curr.prev.val
                b = curr.val
                if tokens[i] == "+":
                    result = a + b
                elif tokens[i] == "-":
                    result = a - b
                elif tokens[i] == "*":
                    result = a * b
                elif tokens[i] == "/":
                    result = int(a / b)
                curr = curr.prev
                curr.val = result
                continue
            curr.next = DoublyLinkedList(int(tokens[i]))
            tmp = curr
            curr = curr.next
            curr.prev = tmp

        return curr.val