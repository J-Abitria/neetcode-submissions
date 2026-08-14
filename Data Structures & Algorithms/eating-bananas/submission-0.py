class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxEatingSpeed = 0

        for pile in piles: maxEatingSpeed = max(maxEatingSpeed, pile)

        minEatingSpeed = maxEatingSpeed
        left = 1
        mid = maxEatingSpeed // 2 + left

        while left <= maxEatingSpeed:
            timeToEat = 0
            for pile in piles:
                timeToEat += math.ceil(pile / mid)
            
            if timeToEat <= h:
                minEatingSpeed = min(minEatingSpeed, mid)
                maxEatingSpeed = mid - 1
            else:
                left = mid + 1
            
            mid = (maxEatingSpeed - left) // 2 + left
        
        return minEatingSpeed
