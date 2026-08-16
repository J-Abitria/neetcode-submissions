# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None: return list2
        elif list2 is None: return list1

        mergedList = curPtr = None
        while list1 is not None and list2 is not None:
            temp = ListNode()
            if list1.val <= list2.val:
                temp.val = list1.val
                list1 = list1.next
            else:
                temp.val = list2.val
                list2 = list2.next
            
            if mergedList is None:
                mergedList = curPtr = temp
            else:
                curPtr.next = temp
                curPtr = curPtr.next
        
        if list1 is not None:
            curPtr.next = list1
        elif list2 is not None:
            curPtr.next = list2
        
        return mergedList

        