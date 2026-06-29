class LRUCache:

    def __init__(self, capacity: int):
        self.hashMap = OrderedDict()
        self.capacity = capacity #Initializing using self so we can use across all functions throughout class with instance memory to self object

    def get(self, key: int) -> int:
        if key in self.hashMap:
            self.hashMap.move_to_end(key)
            return self.hashMap[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self.hashMap[key] = value
            self.hashMap.move_to_end(key)
        else:
            if (len(self.hashMap) >= self.capacity):
                self.hashMap.popitem(last=False)
            self.hashMap[key] = value