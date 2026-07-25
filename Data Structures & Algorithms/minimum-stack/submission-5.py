class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        else:
            return

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return

    def getMin(self) -> int:
        self.minN = float("inf")
        for i in range(len(self.stack)):
            self.minN = min(self.minN, self.stack[i])
        return self.minN

        
