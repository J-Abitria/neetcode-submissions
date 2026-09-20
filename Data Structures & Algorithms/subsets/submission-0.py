class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        possibleSubsets = list()
        curSubset = []

        def traverseList(idx):
            if idx >= len(nums):
                possibleSubsets.append(curSubset.copy())
                return
            
            curSubset.append(nums[idx])
            traverseList(idx + 1)
            curSubset.pop()
            traverseList(idx + 1)
        
        traverseList(0)
        return possibleSubsets