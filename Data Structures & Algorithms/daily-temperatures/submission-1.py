class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        tempStack = []

        """
        The nature of the problem is that we want to track for all elements
        in the temperatures array, for at what point there is a warmer day than it.

        To effectively do so, keep a stack of all of the encountered temperatures that
        don't have a warmer day yet. Once a warmer day is found, keep popping temperatures
        off the stack until it is empty, or the current day is not warmer than the day in
        the stack. Subtract the positions of the current index minus the stack index to find
        the number of days between it and the next warmer day.
        """
        for i in range(len(temperatures)):
            while len(tempStack) > 0 and tempStack[len(tempStack) - 1][0] < temperatures[i]:
                tempPair = tempStack.pop(len(tempStack) - 1)
                answer[tempPair[1]] = i - tempPair[1]
            
            tempStack.append((temperatures[i], i))
        
        return answer

