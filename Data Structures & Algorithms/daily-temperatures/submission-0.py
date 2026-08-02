class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        tempStack = []

        for i in range(len(temperatures)):
            while len(tempStack) > 0 and tempStack[len(tempStack) - 1][0] < temperatures[i]:
                tempPair = tempStack.pop(len(tempStack) - 1)
                answer[tempPair[1]] = i - tempPair[1]
            
            tempStack.append((temperatures[i], i))
        
        return answer

