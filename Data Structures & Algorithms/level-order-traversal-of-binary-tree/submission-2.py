from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        nodesByLevel = list()
        nodeQueue = deque()
        curHeight = 0
        curLevel = []
        nodeQueue.append((root, 0))
        while len(nodeQueue) > 0:
            curNode = nodeQueue.popleft()

            if curNode[1] != curHeight:
                nodesByLevel.append(curLevel)
                curLevel = []
                curHeight += 1
            curLevel.append(curNode[0].val)

            if curNode[0].left is not None:
                nodeQueue.append((curNode[0].left, curHeight + 1))
            if curNode[0].right is not None:
                nodeQueue.append((curNode[0].right, curHeight + 1))
        
        nodesByLevel.append(curLevel)
        return nodesByLevel
