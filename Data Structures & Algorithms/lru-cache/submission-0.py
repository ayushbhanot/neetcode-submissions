class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = OrderedDict() #Library for cache/Hashmap questions


    def get(self, key: int) -> int:
        if key not in self.hashMap:
            return -1
        else:
            self.hashMap.move_to_end(key) #Moves key to most recent used
            return self.hashMap[key]

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self.hashMap[key] = value
            self.hashMap.move_to_end(key)
        else:
            if len(self.hashMap) >= self.capacity:
                self.hashMap.popitem(last=False)
            self.hashMap[key] = value
