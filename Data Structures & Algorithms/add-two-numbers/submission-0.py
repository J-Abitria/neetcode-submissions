# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryOverSum = 0
        curPlace = sumList = None

        while l1 is not None or l2 is not None:
            curSum = carryOverSum
            if l1 is not None:
                curSum += l1.val
                l1 = l1.next
            if l2 is not None:
                curSum += l2.val
                l2 = l2.next
            
            if curPlace is None:
                curPlace = sumList = ListNode(curSum % 10)
            else:
                curPlace.next = ListNode(curSum % 10)
                curPlace = curPlace.next
            
            carryOverSum = curSum // 10
        
        if carryOverSum > 0:
            curPlace.next = ListNode(carryOverSum)
        
        return sumList
        
