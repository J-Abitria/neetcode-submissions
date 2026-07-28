class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        foundNums = {}

        for num in nums:
            if num in foundNums:
                return True

            foundNums[num] = True
        
        return False