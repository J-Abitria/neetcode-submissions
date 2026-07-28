class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        encounteredNums = {}

        for num in nums:
            if num not in encounteredNums:
                encounteredNums[num] = 1
            else:
                return True
        
        return False
        