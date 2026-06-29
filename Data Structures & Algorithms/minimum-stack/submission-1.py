class MinStack:

    def __init__(self):
        self.heap = []
        self.minHeap = []

    def push(self, val: int) -> None:
        self.heap.append(val)

        if not self.minHeap:
            self.minHeap.append(val)
        else:
            self.minHeap.append(min(val, self.minHeap[-1]))

    def pop(self) -> None:
        self.minHeap.pop()
        self.heap.pop()

    def top(self) -> int:
        return self.heap[-1]
        
    def getMin(self) -> int:
        return self.minHeap[-1]
