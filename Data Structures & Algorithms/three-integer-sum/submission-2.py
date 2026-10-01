class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        triplets = list()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break

            first = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if left > i + 1 and nums[left] == nums[left - 1]:
                    left += 1
                    continue
                
                total = first + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    triplets.append([first, nums[left], nums[right]])
                    left += 1
                    right -= 1
        
        return triplets
