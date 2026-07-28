class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        encounteredNums = {}

        for i in range(len(nums)):
            if nums[i] not in encounteredNums:
                encounteredNums[nums[i]] = i
            
            if target - nums[i] in encounteredNums and encounteredNums[target - nums[i]] != i:
                return [encounteredNums[target - nums[i]], i]