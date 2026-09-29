import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(pos, speed) for (pos, speed) in zip(position, speed)])

        numFleets = 1
        fleetTime = (target - cars[-1][0]) / cars[-1][1]
        for i in range(len(cars) - 2, -1, -1):
            curCarTime = (target - cars[i][0]) / cars[i][1]

            if curCarTime > fleetTime:
                fleetTime = curCarTime
                numFleets += 1

        return numFleets