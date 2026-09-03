from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodeQueue = deque()
        nodesByLevel = []

        if root is None:
            return nodesByLevel
        
        nodeQueue.append((root, 0))
        height = 0
        curList = []
        while len(nodeQueue) > 0:
            cur = nodeQueue.popleft()

            if cur[1] != height:
                nodesByLevel.append(curList)
                curList = []
                height = cur[1]
            curList.append(cur[0].val)
            
            if cur[0].left is not None:
                nodeQueue.append((cur[0].left, cur[1] + 1))
            if cur[0].right is not None:
                nodeQueue.append((cur[0].right, cur[1] + 1))
        
        nodesByLevel.append(curList)
        
        return nodesByLevel
    