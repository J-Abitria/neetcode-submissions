from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        createdNodes = dict()
        def dfs(curNode):
            if curNode.val in createdNodes:
                return createdNodes[curNode.val]
            
            nodeCopy = Node(curNode.val)
            createdNodes[curNode.val] = nodeCopy
            for neighbor in curNode.neighbors:
                nodeCopy.neighbors.append(dfs(neighbor))
            
            return nodeCopy
        
        return dfs(node)