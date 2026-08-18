import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heapSize = k
        self.numHeap = []
        for num in nums:
            heapq.heappush(self.numHeap, num)
        
        while len(self.numHeap) > k:
            heapq.heappop(self.numHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.numHeap, val)

        if len(self.numHeap) > self.heapSize:
            heapq.heappop(self.numHeap)
        
        return self.numHeap[0]