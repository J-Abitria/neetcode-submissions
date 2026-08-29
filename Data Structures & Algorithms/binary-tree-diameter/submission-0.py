# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0

        def depthFirstSearch(root: Optional[TreeNode]):
            nonlocal maxDiameter

            if root is None:
                return 0

            left = depthFirstSearch(root.left)
            right = depthFirstSearch(root.right)
            maxDiameter = max(maxDiameter, left + right)

            return 1 + max(left, right)
        
        depthFirstSearch(root)
        return maxDiameter