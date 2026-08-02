import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sorting by position of the cars to simulate where they are on the road,
        # makes the one pass iteration easier.
        sortedCars = sorted([(position[i], speed[i]) for i in range(len(position))])

        fleets = 0
        curMaxFleetTime = 0

        """Keeping the current max fleet time allows for storing the
        time it takes for the current fleet to reach the end.
        If the next car checked takes longer to reach the end
        than the current fleet, then it must be a new fleet."""
        for i in range(len(sortedCars) - 1, -1, -1):
            carTime = (target - sortedCars[i][0]) / sortedCars[i][1]

            if carTime > curMaxFleetTime:
                fleets += 1
                curMaxFleetTime = carTime
        
        return fleets