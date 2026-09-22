class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = list()
        candidates.sort()

        def dfs(i, combo, curSum):
            if curSum == target:
                combinations.append(combo.copy())
                return

            if curSum > target or i >= len(candidates):
                return
            
            for j in range(i, len(candidates)):
                # Handles duplicates that are found later in the candidates list.
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                
                combo.append(candidates[j])
                dfs(j + 1, combo, curSum + candidates[j])
                combo.pop()
        
        dfs(0, [], 0)
        return combinations