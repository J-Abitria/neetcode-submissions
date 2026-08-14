import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start, end = 1, k
        numHeap = []
        answer = []

        for i in range(k):
            heapq.heappush(numHeap, (-1 * nums[i], i))
        answer.append(-1 * numHeap[0][0])
        
        while end < len(nums):
            heapq.heappush(numHeap, (-1 * nums[end], end))
            while len(numHeap) > 0 and numHeap[0][1] < start:
                heapq.heappop(numHeap)
            
            answer.append(-1 * numHeap[0][0])
            start += 1
            end += 1
        
        return answer
