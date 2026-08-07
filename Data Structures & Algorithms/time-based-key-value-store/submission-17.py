class TimeMap:

    def __init__(self):
        self.TimeMap = {} #O(1) time and space for each call

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.TimeMap:
            self.TimeMap[key] = []
        self.TimeMap[key].append((timestamp, value)) #O(1) time and space for each call
#But to store all time stamp values to a key it will take O(unique keys * unique timestamps) space and same for time to store all of them
    def get(self, key: str, timestamp: int) -> str:
        
        res = ""

        if key not in self.TimeMap:
            return res

        history = self.TimeMap[key]

        l, r = 0, len(history) - 1

        while l <= r:
            m = l + (r - l) // 2

            if history[m][0] == timestamp:
                res = history[m][1]
                break
            
            elif timestamp < history[m][0]:
                r = m - 1
            
            elif timestamp >= history[m][0]:
                res = history[m][1]
                l = m + 1
            
        return res #O(lognumber of timestamps in key) time and O(1) space for get 
