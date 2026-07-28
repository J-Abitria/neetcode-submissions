class Solution:
    # O(n log n) time complexity.
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # A list of encountered values.
        encounteredNums = {}

        # Runs over the whole length of the array in O(n) time.
        for i in range(len(nums)):
            # Since the goal is nums[i] + nums[j] = target, taking
            # target - nums[i] will provide the goal nums[j], which is searched
            # for in the map in O(log n) time.
            if target - nums[i] in encounteredNums:
                # If found, return the map index first as it was found before
                # index i.
                return [encounteredNums[target - nums[i]], i]
            else:
                encounteredNums[nums[i]] = i
        