import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = [root.val]

        def dfs(root):
            if root is None:
                return 0
            
            leftVal = max(dfs(root.left), 0)
            rightVal = max(dfs(root.right), 0)

            maxSum[0] = max(maxSum[0], root.val + leftVal + rightVal)
            return root.val + max(leftVal, rightVal)
        
        dfs(root)
        return maxSum[0]