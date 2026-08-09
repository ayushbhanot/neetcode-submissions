# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        beforeHead = ListNode(0, None)

        curr = beforeHead

        while list1 and list2:
            if list2.val < list1.val:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
            else:
                curr.next = list1
                curr = curr.next
                list1 = list1.next

        while list1:
            curr.next = list1
            curr = curr.next
            list1 = list1.next

        while list2:
            curr.next = list2
            curr = curr.next
            list2 = list2.next #O(N) time and O(n) space but O(1) auxillary space?

        return beforeHead.next