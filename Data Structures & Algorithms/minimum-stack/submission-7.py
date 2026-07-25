class MinStack:

    def __init__(self):
        self.stack = [] #O(1) time

    def push(self, val: int) -> None:
        self.stack.append(val) #O(1) time

    def pop(self) -> None:
        if self.stack:
            self.stack.pop() #O(1) time
        else:
            return

    def top(self) -> int:
        if self.stack:
            return self.stack[-1] #O(1) time
        else:
            return

    def getMin(self) -> int:
        minimum = float("inf")
        tmp = []
        while len(self.stack): #O(n) time and space
            minimum = min(minimum, self.stack[-1])
            tmp.append(self.stack.pop())

        while len(tmp): #O(n) time again
            self.stack.append(tmp.pop())

        return minimum