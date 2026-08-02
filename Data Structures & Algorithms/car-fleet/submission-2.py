import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedCars = sorted([(position[i], speed[i]) for i in range(len(position))])

        fleets = 0
        curMaxFleetTime = 0
        for i in range(len(sortedCars) - 1, -1, -1):
            carTime = (target - sortedCars[i][0]) / sortedCars[i][1]

            if carTime > curMaxFleetTime:
                fleets += 1
                curMaxFleetTime = carTime
        
        return fleets