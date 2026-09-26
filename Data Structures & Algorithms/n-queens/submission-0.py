class Solution:
    def isPlaceable(self, row, col, board):
        for i in range(col):
            if board[row][i] == "Q":
                return False
        
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            
            r -= 1
            c -= 1
        
        r, c = row + 1, col - 1
        while r < len(board) and c >= 0:
            if board[r][c] == "Q":
                return False
            
            r += 1
            c -= 1
        
        return True

    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = list()
        solution = ["." * n] * n

        def dfs(col):
            if col == n:
                solutions.append(solution.copy())
                return

            for i in range(n):
                if self.isPlaceable(i, col, solution):
                    solution[i] = solution[i][:col] + "Q" + solution[i][col + 1:]
                    dfs(col + 1)
                    solution[i] = "." * n
        dfs(0)

        return solutions