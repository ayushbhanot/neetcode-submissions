class MinStack:

    def __init__(self):
        self.stack = []
        self.minHeap = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minHeap and val > self.minHeap[-1]:
            self.minHeap.append(self.minHeap[-1])  
        else:
            self.minHeap.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minHeap.pop()

    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.minHeap[-1]
