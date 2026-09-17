from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqTable = [0] * 26
        for task in tasks:
            freqTable[ord(task) - ord('A')] += 1

        maxHeap = []
        for i in range(len(freqTable)):
            if freqTable[i] > 0:
                heapq.heappush_max(maxHeap, (freqTable[i], chr(ord('A') + i)))
        print(maxHeap)
        
        time = 0
        taskQueue = deque()
        while len(maxHeap) > 0 or len(taskQueue) > 0:
            if len(maxHeap) == 0:
                time = taskQueue[0][0]
            
            if len(taskQueue) > 0 and time >= taskQueue[0][0]:
                freedTask = taskQueue.popleft()
                heapq.heappush_max(maxHeap, (freedTask[1], freedTask[2]))
            
            task = heapq.heappop_max(maxHeap)
            time += 1
            if task[0] - 1 > 0:
                taskQueue.append((time + n, task[0] - 1, task[1]))
            

        return time