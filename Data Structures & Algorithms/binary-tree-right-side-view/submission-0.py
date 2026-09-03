from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        answer = []
        nodeQueue = deque([(root, 0)])
        height = 0
        while len(nodeQueue) > 0:
            cur = nodeQueue.popleft()

            if cur[0].left is not None:
                nodeQueue.append((cur[0].left, cur[1] + 1))
            if cur[0].right is not None:
                nodeQueue.append((cur[0].right, cur[1] + 1))
            
            if len(nodeQueue) == 0 or nodeQueue[0][1] > height:
                answer.append(cur[0].val)
                height += 1
        
        return answer