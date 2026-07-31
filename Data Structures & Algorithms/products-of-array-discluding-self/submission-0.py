class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] + [0] * (len(nums) - 1)

        for i in range(1, len(nums)):
            answer[i] = answer[i - 1] * nums[i - 1]
        
        """ 
        The backtrackingVal acts as if you had the second array:
        - The better solution is having two arrays:
            one with setup [1, 0, 0, ...]
            the other with [0, 0, ..., 1]

            For the first array, you multiply the element on the
            left of your current index of the array with the 
            element in the nums array at the left of the current index.
            
            Do the same on the second array, except take elements on the right.
            Then, multiply the values at each element from the 2 arrays together.

        backtrackingVal acts as that second temporary array, since by this point,
        the answer array is formatted like the first temporary array, and you only
        need the most recently computed answer of the second temporary array.
        """
        backtrackingVal = 1
        for i in range(len(nums) - 2, -1, -1):
            answer[i] *= backtrackingVal * nums[i + 1]
            backtrackingVal *= nums[i + 1]
        
        return answer