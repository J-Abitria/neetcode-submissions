# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        numGoodNodes = 0

        def dfs(root: TreeNode, largestValue: int):
            nonlocal numGoodNodes

            if root is None:
                return
            
            if root.val >= largestValue:
                numGoodNodes += 1
                largestValue = root.val
            
            dfs(root.left, largestValue)
            dfs(root.right, largestValue)
        
        dfs(root, root.val)
        return numGoodNodes