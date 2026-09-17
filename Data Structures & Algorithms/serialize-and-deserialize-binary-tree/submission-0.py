# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        
        def dfs(root):
            if root is None:
                return "N"

            return str(root.val) + "," + dfs(root.left) + "," + dfs(root.right)
        
        tree = dfs(root)
        return tree
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        
        values = data.split(",")
        idx = 0
        def dfs(values):
            nonlocal idx
            if values[idx] == "N":
                return None
            
            root = TreeNode(int(values[idx]))
            idx += 1
            root.left = dfs(values)
            idx += 1
            root.right = dfs(values)

            return root
        
        tree = dfs(values)
        return tree

