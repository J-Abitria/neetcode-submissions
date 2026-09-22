class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = list()

        def dfs(i, perm, usedNums):
            print(perm)
            if len(perm) == len(nums):
                permutations.append(perm.copy())
                return
            
            if i >= len(nums):
                return
            
            for j in range(len(nums)):
                if usedNums[j]:
                    continue
                
                perm.append(nums[j])
                usedNums[j] = True
                # For each branch of the decision, you have to start at the beginning again to
                # catch any numbers earlier in the list that are not in the current permutation.
                dfs(0, perm, usedNums)
                perm.pop()
                usedNums[j] = False

        dfs(0, list(), [False] * len(nums))

        return permutations