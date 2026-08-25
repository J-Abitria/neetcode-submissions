# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        secondHalf = slow.next
        prevNode = slow.next = None
        while secondHalf is not None:
            temp = secondHalf.next
            secondHalf.next = prevNode
            prevNode = secondHalf
            secondHalf = temp

        firstHalf, secondHalf = head, prevNode
        while firstHalf is not None and secondHalf is not None:
            temp1, temp2 = firstHalf.next, secondHalf.next
            firstHalf.next = secondHalf
            secondHalf.next = temp1
            firstHalf, secondHalf = temp1, temp2