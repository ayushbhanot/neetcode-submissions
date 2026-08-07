class TimeMap:

    def __init__(self):
        self.TimeMap = {} #O(1) time and space

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.TimeMap:
            self.TimeMap[key] = []
        self.TimeMap[key].append((timestamp, value)) #O(1) time and space

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.TimeMap:
            return ""
        history = self.TimeMap[key]
                                    #   0
        l, r = 0, len(history) - 1 #[(10, value1)]

        while l < r:
            m = l + (r - l) // 2

            if history[m][0] == timestamp:  #0          1       2
                return history[m][1]  #[(10, one), (20, two), (30, three)]

            elif history[m][0] < timestamp:
                if history[m + 1][0] > timestamp:
                    return history[m][1]
                else:
                    l = m + 1
            elif history[m][0] > timestamp:
                r = m
        
        if history[l][0] <= timestamp:
            return history[l][1]
        else:
            return ""