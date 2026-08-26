# Definition for a Node.
class Node:
    def __init__(self, x: int, next: Node = None, random: Node = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if head is None:
            return None
        
        copiedNodes = dict()
        copiedNodes[None] = None
        curNode = head
        while curNode is not None:
            copiedNodes[curNode] = Node(curNode.val)
            curNode = curNode.next
        
        curCopy = headCopy = copiedNodes[head]
        curNode = head
        while curNode is not None:
            curCopy.next = copiedNodes[curNode.next]
            curCopy.random = copiedNodes[curNode.random]
            curCopy = curCopy.next
            curNode = curNode.next
        
        return headCopy

