# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        foundVal = 0
        curPos = 0

        def dfs(root):
            nonlocal foundVal
            nonlocal curPos

            if root is None:
                return
            
            dfs(root.left)
            
            curPos += 1
            if curPos == k:
                foundVal = root.val
                return
            
            dfs(root.right)
        
        dfs(root)
        return foundVal