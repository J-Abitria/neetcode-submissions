class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] + [0] * (len(nums) - 1)

        for i in range(1, len(nums)):
            answer[i] = nums[i - 1] * answer[i - 1]
        
        backwardsProduct = 1
        for i in range(len(nums) - 2, -1, -1):
            backwardsProduct *= nums[i + 1]
            answer[i] *= backwardsProduct
        
        return answer