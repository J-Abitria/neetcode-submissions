class Solution:
    def trap(self, height: List[int]) -> int:
        leftSideMax = [height[0]] + [0] * (len(height) - 1)
        rightSideMax = [0] * (len(height) - 1) + [height[-1]]
        rainWater = 0

        # We need to dynamically track the max at each point, in case there is a scenario in which
        # the max is found, but there are additional pockets of rain water that
        # can be discovered.
        for i in range(1, len(height)):
            leftSideMax[i] = max(leftSideMax[i - 1], height[i])
        
        for i in range(len(height) - 2, -1, -1):
            rightSideMax[i] = max(rightSideMax[i + 1], height[i])
        
        for i in range(len(height)):
            trappedWater = min(leftSideMax[i], rightSideMax[i]) - height[i]
            if trappedWater > 0: rainWater += trappedWater
        
        return rainWater