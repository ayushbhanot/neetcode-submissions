class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [0] #Random value for 0-index
        self.k = k
        for j in range(len(nums)):
            self.push(nums[j])
        while len(self.heap) - 1 > self.k:
            self.pop()

        

    def add(self, val: int) -> int:
        self.push(val)
        if len(self.heap) - 1 > self.k:
            self.pop()
        return self.heap[1]

        
    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 1 and (self.heap[i//2] > self.heap[i]):
            tmp = self.heap[i//2]
            self.heap[i//2] = self.heap[i]
            self.heap[i] = tmp
            i = i//2
    
    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1] #Store temporarily what we want to pop so we can return it later
        self.heap[1] = self.heap.pop() #Replace root with last Popped Node
        i = 1 #Set index
        while (i * 2 < len(self.heap)): #While left child exists
            if (i * 2 + 1 < len(self.heap) and self.heap[i * 2 + 1] < self.heap[i] and self.heap[i * 2 + 1] < self.heap[i * 2]):
                tmp = self.heap[i]
                self.heap[i] = self.heap[i * 2 + 1]
                self.heap[i * 2 + 1] = tmp
                i = i * 2 + 1
            elif (self.heap[i * 2] < self.heap[i]):
                tmp = self.heap[i]
                self.heap[i] = self.heap[i * 2]
                self.heap[i * 2] = tmp
                i = i * 2
            else:
                break
        return res
