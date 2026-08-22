class Node:
    def __init__(self, val, key=None, next=None, prev=None):
        self.val = val
        self.key = key
        self.next, self.prev = next, prev

class LRUCache:

    def __init__(self, capacity: int):
        self.Map = {}
        self.capacity = capacity
        self.dummyHead, self.dummyTail = Node(0), Node(0)
        self.dummyHead.next, self.dummyTail.prev = self.dummyTail, self.dummyHead

    def get(self, key: int) -> int:
        if key in self.Map: #Return the value for that key but you have to  make it most Recently used
            node = self.Map[key]
            Prev, Next = node.prev, node.next
            Prev.next, Next.prev = Next, Prev
            node.next, node.prev = None, None
            self.Map[key] = self.append(node.val, key)
            return self.Map[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.Map:
            node = self.Map[key]
            Prev, Next = node.prev, node.next
            Prev.next, Next.prev = Next, Prev
            node.next, node.prev = None, None
        self.Map[key] = self.append(value, key)
        if len(self.Map) > self.capacity:
            key = self.removeLRN()
            self.Map.pop(key)
        return

    def append(self, val: int, key: int):
        oldTail = self.dummyTail.prev
        newTail = Node(val, key)
        oldTail.next = newTail
        newTail.next, newTail.prev = self.dummyTail, oldTail
        self.dummyTail.prev = newTail
        return newTail

    def removeLRN(self):
        LRN = self.dummyHead.next
        key = LRN.key
        newHead = LRN.next
        self.dummyHead.next, newHead.prev = newHead, self.dummyHead
        LRN.next, LRN.prev = None, None
        return key