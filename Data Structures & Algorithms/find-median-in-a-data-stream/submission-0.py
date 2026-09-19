class MedianFinder:

    def __init__(self):
        self.nums = list()

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()
        medianIndex = len(self.nums) // 2

        if len(self.nums) % 2 != 0:
            return self.nums[medianIndex]
        
        return (self.nums[medianIndex - 1] + self.nums[medianIndex]) / 2
        