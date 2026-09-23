class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = list()

        def dfs(numOpen, numClosed, parentheses):
            if numOpen + numClosed == 2 * n:
                combinations.append(parentheses)
                return
            
            if numOpen < n:
                parentheses += "("
                dfs(numOpen + 1, numClosed, parentheses)
                parentheses = parentheses[:-1]
            
            if numClosed < numOpen:
                parentheses += ")"
                dfs(numOpen, numClosed + 1, parentheses)
                parentheses = parentheses[:-1]
        dfs(0, 0, "")

        return combinations
