# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None

        reversedList = ListNode(head.val)

        while head.next is not None:
            head = head.next
            temp = ListNode(head.val)
            temp.next = reversedList
            reversedList = temp
        
        return reversedList