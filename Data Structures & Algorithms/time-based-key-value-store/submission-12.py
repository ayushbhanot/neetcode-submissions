class TimeMap:

    def __init__(self):
        self.TimeMap = {} #O(1) time and space

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.TimeMap:
            self.TimeMap[key] = []
        self.TimeMap[key].append((timestamp, value)) #O(1) time and space

    def get(self, key: str, timestamp: int) -> str:
        
        res = ""

        if key not in self.TimeMap:
            return res

        history = self.TimeMap[key]

        l, r = 0, len(history) - 1

        while l < r:

            m = l + (r - l) // 2

            if history[m][0] == timestamp:#(10, one),(20, two),(30, three)
                return history[m][1]

            if history[m][0] > timestamp:
                r = m - 1
            elif history[m][0] < timestamp:
                res = history[m][1]
                l = m + 1
        
        if history[l][0] <= timestamp:
            return history[l][1]

        return res