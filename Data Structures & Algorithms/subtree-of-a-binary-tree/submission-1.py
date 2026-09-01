# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None and root2 is None:
            return True
        
        if root1 is None or root2 is None or root1.val != root2.val:
            return False
        
        return self.sameTree(root1.left, root2.left) and self.sameTree(root1.right, root2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        
        isSameTree = False
        if root.val == subRoot.val:
            isSameTree = self.sameTree(root, subRoot)
        
        return isSameTree or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)