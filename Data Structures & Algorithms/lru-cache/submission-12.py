class Node:
    def __init__(self, val, key=None, next=None, prev=None):
        self.val = val
        self.next, self.prev = next, prev
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.Map = {}
        self.capacity = capacity
        self.dummyHead = Node(0)
        self.dummyTail = Node(0)
        self.dummyHead.next, self.dummyTail.prev = self.dummyTail, self.dummyHead

    def get(self, key: int) -> int:
        if key in self.Map:
            node = self.Map[key]
            self.remove(node)
            self.append(node)
            return self.Map[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.Map:
            self.remove(self.Map[key])
        self.Map[key] = Node(value, key)
        self.append(self.Map[key])
        if len(self.Map) > self.capacity:
            head = self.dummyHead.next
            self.remove(self.dummyHead.next)
            self.Map.pop(head.key)

    def append(self, node: Node):
        oldTail = self.dummyTail.prev
        node.next, node.prev = self.dummyTail, oldTail
        oldTail.next, self.dummyTail.prev = node, node

    def remove(self, node: Node):
        Prev, Next = node.prev, node.next
        Prev.next, Next.prev = Next, Prev
        node.next, node.prev = None, None

