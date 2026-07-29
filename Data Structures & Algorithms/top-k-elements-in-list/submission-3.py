import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if (k == len(nums)): return nums

        numFreq = {}

        for num in nums:
            if num in numFreq:
                numFreq[num] += 1
            else:
                numFreq[num] = 0
        
        numHeap = []
        for num in numFreq:
            heapq.heappush(numHeap, (numFreq[num], num))
            
            if len(numHeap) > k:
                heapq.heappop(numHeap)
        
        return [pair[1] for pair in numHeap]

        

