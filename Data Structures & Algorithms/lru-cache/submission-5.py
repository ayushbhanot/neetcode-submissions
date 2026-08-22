class LRUCache:

    def __init__(self, capacity: int):
        self.Map = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.Map:
            val = self.Map.pop(key)
            self.Map[key] = val
            return self.Map[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.Map:
            self.Map.pop(key)
        self.Map[key] = value

        while len(self.Map) > self.capacity:
            oldestKey = next(iter(self.Map))
            self.Map.pop(oldestKey)

        

