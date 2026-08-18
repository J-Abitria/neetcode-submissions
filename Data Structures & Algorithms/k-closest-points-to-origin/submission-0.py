import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        coordHeap = []

        for point in points:
            heapq.heappush(coordHeap, (-1 * (point[0] ** 2 + point[1] ** 2) ** 0.5, point))

            if len(coordHeap) > k:
                heapq.heappop(coordHeap)
        
        return [coord for _, coord in coordHeap]