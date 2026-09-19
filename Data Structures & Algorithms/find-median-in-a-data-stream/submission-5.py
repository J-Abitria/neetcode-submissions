import heapq

class MedianFinder:

    def __init__(self):
       self.leftHeap = list()
       self.rightHeap = list()

    def addNum(self, num: int) -> None:
        parity = (len(self.leftHeap) + len(self.rightHeap)) % 2

        numToInsert = num
        if parity == 0:
            # Then we must grow the right heap.
            numToInsert = num
            if len(self.leftHeap) > 0 and self.leftHeap[0] > num:
                numToInsert = heapq.heappop_max(self.leftHeap)
                heapq.heappush_max(self.leftHeap, num)
            
            heapq.heappush(self.rightHeap, numToInsert)
        else:
            # Then we must grow the left heap. We can now assume that the right heap is not empty.
            numToInsert = num
            if self.rightHeap[0] < num:
                numToInsert = heapq.heappop(self.rightHeap)
                heapq.heappush(self.rightHeap, num)
            
            heapq.heappush_max(self.leftHeap, numToInsert)

    def findMedian(self) -> float:
        if (len(self.leftHeap) + len(self.rightHeap)) % 2 == 0:
            return (self.leftHeap[0] + self.rightHeap[0]) / 2
        
        return self.rightHeap[0]
        
        