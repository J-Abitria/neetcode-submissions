from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottenBananas = deque([])
        minutes = 0
        freshBananas = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    freshBananas += 1
                elif grid[i][j] == 2:
                    rottenBananas.append((i, j, minutes))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while len(rottenBananas) > 0:
            curCell = rottenBananas.popleft()

            for direction in directions:
                newRow, newCol, minutes = curCell[0] + direction[0], curCell[1] + direction[1], curCell[2]

                if newRow < 0 or newRow >= len(grid) or newCol < 0 or newCol >= len(grid[i]):
                    continue
                
                if grid[newRow][newCol] == 1:
                    grid[newRow][newCol] = 2
                    freshBananas -= 1
                    rottenBananas.append((newRow, newCol, minutes + 1))
        
        return minutes if freshBananas == 0 else -1