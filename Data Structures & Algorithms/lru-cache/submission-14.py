class LRUCache:

    def __init__(self, capacity: int):
        self.Map = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.Map:
            value = self.Map[key]
            self.Map.pop(key)
            self.Map[key] = value
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.Map:
            self.Map.pop(key)
        self.Map[key] = value
        if len(self.Map) > self.capacity:
            oldestKey = next(iter(self.Map))
            self.Map.pop(oldestKey) #O(1) time and O(n) space O(1) auxillary but the thing is this is not how hashmaps generally work they are not ordered by any means by default just in python 3.7+ they are iordered by insertion so i'm taking advantage of that