class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = [] #O(1) time

    def push(self, val: int) -> None:
        if self.stack:
            minimum = min(self.minStack[-1], val)
            self.minStack.append(minimum)
        else:
            self.minStack.append(val)
        self.stack.append(val) #O(1) time and space for this function

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minStack.pop()
        else:
            return

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return #O(1) time

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        else:
            return #O(1) time
