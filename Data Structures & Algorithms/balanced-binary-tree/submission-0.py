# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True

        def depthFirstSearch(root: Optional[TreeNode]):
            nonlocal isBalanced

            if root is None:
                return 0

            leftHeight = 1 + depthFirstSearch(root.left)
            rightHeight = 1 + depthFirstSearch(root.right)

            if abs(leftHeight - rightHeight) > 1:
                isBalanced = False
            
            return max(leftHeight, rightHeight)
        
        depthFirstSearch(root)
        return isBalanced