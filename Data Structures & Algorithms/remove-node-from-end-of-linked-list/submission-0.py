# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        index = 0
        temp = head
        while temp is not None:
            temp = temp.next
            index += 1

        startOfList = curNode = head
        prevNode = None

        while index > n:
            temp = curNode.next
            prevNode = curNode
            curNode = temp
            index -= 1
        
        if prevNode is None:
            startOfList = curNode.next
        else:
            prevNode.next = curNode.next
        del curNode

        return startOfList