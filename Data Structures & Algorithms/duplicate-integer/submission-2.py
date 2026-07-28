class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        encounteredNums = {}

        for num in nums:
            if num in encounteredNums:
                return True
            
            encounteredNums[num] = True

        return False