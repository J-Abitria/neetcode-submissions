class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = list()

        def dfs(i, curCombination, total):
            if total == target:
                combinations.append(curCombination.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            curCombination.append(nums[i])
            dfs(i, curCombination, total + nums[i])
            curCombination.pop()
            dfs(i + 1, curCombination, total)
        
        dfs(0, list(), 0)
        return combinations