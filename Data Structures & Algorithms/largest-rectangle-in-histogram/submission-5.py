class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        indexStack = []
        heightStack = []
        maxArea = 0

        for i in range(len(heights)):
            # Setting the left boundary as the current bar to analyze, in case it is
            # the farthest left the current bar can stretch.
            leftBoundary = i

            while len(indexStack) > 0 and heights[i] < heightStack[-1]:
                idx = indexStack.pop()
                height = heightStack.pop()

                # Calculating the area by using the height on the stack,
                # and using the value i as the right boundary, and idx
                # as the left boundary of the width.
                maxArea = max(maxArea, height * (i - idx))

                # Updates the new farthest left boundary, as if heights[i]
                # is less than the current height from the stack, it stretches
                # left at least as far as the current index from the stack.
                leftBoundary = idx
            
            indexStack.append(leftBoundary)
            heightStack.append(heights[i])
        
        while len(indexStack) > 0:
            idx = indexStack.pop()
            height = heightStack.pop()
            maxArea = max(maxArea, height * (len(heights) - idx))
        
        return maxArea
            

        