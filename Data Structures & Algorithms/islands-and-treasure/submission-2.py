from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2 ** 31 - 1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        tileQueue = deque()

        # Separates responsibility of setting up BFS by running a loop over the grid to find all
        # treasures first.
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    tileQueue.append((i, j))

        # Once the treasure locations are all known, now run BFS using each treasure as a reference point.
        # This prevents super nested loops.
        while len(tileQueue) > 0:
            row, col = tileQueue.popleft()
            for direction in directions:
                newRow, newCol = row + direction[0], col + direction[1]
                if newRow < 0 or newRow >= len(grid) or newCol < 0 or newCol >= len(grid[0]):
                    continue
                if grid[newRow][newCol] == INF:
                    # Because BFS always starts at a treasure, any adjacent land tiles will have their distance
                    # set to 1 (0 + 1), which through DP saves the distance for every tile adjacent to a land tile
                    # of distance 1, and so on.
                    grid[newRow][newCol] = grid[row][col] + 1
                    tileQueue.append((newRow, newCol))
