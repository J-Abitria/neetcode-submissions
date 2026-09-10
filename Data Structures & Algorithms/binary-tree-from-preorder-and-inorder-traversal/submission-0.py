# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        treeNodes = dict()

        for i in range(len(inorder)):
            treeNodes[inorder[i]] = i
        
        curIdx = 0
        def dfs(left, right):
            nonlocal curIdx

            if left > right:
                return None
            
            root = TreeNode(preorder[curIdx])
            curIdx += 1
            mid = treeNodes[root.val]
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(inorder) - 1)


