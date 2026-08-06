class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # The constraints are within a few thousand entries,
        # so I can safely use an O(n log n) sort.
        nums.sort()
        answer = []
        i = 0
        prevValue = 1

        while i < len(nums) - 2 and nums[i] <= 0:
            if nums[i] == prevValue:
                i += 1
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                # Performing two sum for the left and right values.
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                # We want all possible triplets, and the current value
                # nums[i] could have multiple triplets associated.
                else:
                    answer.append([nums[i], nums[left], nums[right]])
                    left += 1
                    # This additional step prevents duplicate second values. The right
                    # side is irrelevant, as so long as the next pair is distinct, it
                    # doesn't matter which side.
                    while left < right and nums[left] == nums[left - 1]: left += 1

                    right -= 1

            # Updates the previous value to prevent evaluating duplicate first values.
            prevValue = nums[i]
            i += 1
        
        return answer