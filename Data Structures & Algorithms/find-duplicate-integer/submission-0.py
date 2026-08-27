class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        foundNums = dict()

        for num in nums:
            if num in foundNums:
                return num
            
            foundNums[num] = True