# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getKthNode(self, prevGroup, k):
        for i in range(k):
            prevGroup = prevGroup.next
            if prevGroup is None:
                return None
        
        return prevGroup

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevGroup = dummy

        while prevGroup is not None:
            kthNode = self.getKthNode(prevGroup, k)
            if kthNode is None:
                break
            
            nextGroup = kthNode.next
            prev = kthNode.next
            cur = prevGroup.next

            while cur != nextGroup:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            
            temp = prevGroup.next
            prevGroup.next = kthNode
            prevGroup = temp
        
        return dummy.next