class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            height = min(heights[left], heights[right])
            maxArea = max(maxArea, height * (right - left))

            # This condition of which pointer should move is to attempt to
            # find a new bar that is larger.
            if heights[left] < heights[right]: left += 1
            else: right -= 1
        
        return maxArea