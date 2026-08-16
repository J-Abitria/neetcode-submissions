class TimeMap:

    def __init__(self):
        self.timeMap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = [(value, timestamp)]
        else:
            self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap or self.timeMap[key][0][1] > timestamp:
            return ""
        
        left, right = 0, len(self.timeMap[key]) - 1
        maxValIdx = 0
        while left <= right:
            mid = (left + right) // 2
            if self.timeMap[key][mid][1] == timestamp:
                return self.timeMap[key][mid][0]
            elif self.timeMap[key][mid][1] < timestamp:
                if self.timeMap[key][mid][1] > self.timeMap[key][maxValIdx][1]:
                    maxValIdx = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return self.timeMap[key][maxValIdx][0]

