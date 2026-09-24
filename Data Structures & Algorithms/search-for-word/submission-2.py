class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        wordExists = False

        def dfs(coords, idx, visitedCells):
            if idx == len(word):
                return True
            
            outOfBounds = coords[0] < 0 or coords[1] < 0 or coords[0] >= len(board) or coords[1] >= len(board[0])
            if outOfBounds or board[coords[0]][coords[1]] != word[idx] or coords in visitedCells:
                return False
            
            foundPath = False
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            visitedCells.add(coords)
            for direction in directions:
                newCoords = (coords[0] + direction[0], coords[1] + direction[1])
                foundPath = foundPath or dfs(newCoords, idx + 1, visitedCells)
            visitedCells.remove(coords)

            return foundPath

        for i in range(len(board)):
            for j in range(len(board[i])):
                wordExists = dfs((i, j), 0, set())

                if wordExists:
                    return True
        
        return False