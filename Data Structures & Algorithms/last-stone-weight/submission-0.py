import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []

        for stone in stones:
            heapq.heappush(maxHeap, -1 * stone)
        
        while len(maxHeap) > 1:
            first, second = -1 * heapq.heappop(maxHeap), -1 * heapq.heappop(maxHeap)

            if first == second:
                continue
            else:
                heapq.heappush(maxHeap, -1 * (first - second))
        
        if len(maxHeap) == 1:
            return -1 * maxHeap[0]
        
        return 0