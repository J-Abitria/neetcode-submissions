class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxProfit = 0

        while right < len(prices):
            # If there is theoretical profit to be made, check if the
            # profit is larger than the current max, and move the right pointer.
            if prices[right] > prices[left]:
                maxProfit = max(maxProfit, prices[right] - prices[left])
                right += 1
            # Otherwise, reset the left pointer to the new right as it is smaller.
            else:
                left = right
                right += 1
        
        return maxProfit