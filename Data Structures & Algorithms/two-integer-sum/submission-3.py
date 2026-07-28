class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndices = {}

        for i in range(len(nums)):
            if target - nums[i] in numIndices:
                return [numIndices[target - nums[i]], i]
            
            numIndices[nums[i]] = i
        
        return []
