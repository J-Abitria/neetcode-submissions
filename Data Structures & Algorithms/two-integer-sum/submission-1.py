class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        encounteredNums = {}

        for i in range(len(nums)):
            if target - nums[i] in encounteredNums:
                return [encounteredNums[target - nums[i]], i]
            else:
                encounteredNums[nums[i]] = i
        