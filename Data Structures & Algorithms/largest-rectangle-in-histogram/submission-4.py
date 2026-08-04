class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        indexStack = []
        heightStack = []
        maxArea = 0

        for i in range(len(heights)):
            startIdx = i

            while len(indexStack) > 0 and heights[i] < heightStack[-1]:
                idx = indexStack.pop(len(indexStack) - 1)
                area = heightStack.pop(len(heightStack) - 1) * (i - idx)
                maxArea = max(maxArea, area)
                startIdx = idx
            
            indexStack.append(startIdx)
            heightStack.append(heights[i])
        
        while len(indexStack) > 0:
            idx = indexStack.pop(len(indexStack) - 1)
            area = heightStack.pop(len(heightStack) - 1) * (len(heights) - idx)
            maxArea = max(maxArea, area)
        
        return maxArea
        