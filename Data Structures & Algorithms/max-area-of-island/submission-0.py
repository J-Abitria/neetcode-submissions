class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxIslandSize = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0:
                return 0

            grid[row][col] = 0

            return 1 + dfs(row - 1, col) + dfs(row + 1, col) + dfs(row, col - 1) + dfs(row, col + 1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue

                maxIslandSize = max(maxIslandSize, dfs(i, j))
        
        return maxIslandSize
        