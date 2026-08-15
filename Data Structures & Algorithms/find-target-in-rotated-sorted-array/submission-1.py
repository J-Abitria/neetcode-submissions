class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        maxValIdx = 0

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[maxValIdx]: maxValIdx = mid

            if nums[right] >= nums[mid]:
                if nums[right] > nums[maxValIdx]: maxValIdx = right
                right = mid - 1
            else:
                left = mid + 1
        
        print(maxValIdx)
        if target <= nums[maxValIdx] and target >= nums[0]:
            left, right = 0, maxValIdx
        else:
            left, right = maxValIdx + 1, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: return mid
            elif nums[mid] < target: left = mid + 1
            else: right = mid - 1
        
        return -1
        