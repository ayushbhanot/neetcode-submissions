# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0, None)

        curr = dummy

        def helper(curr, list1, list2):
            if not list1 and not list2:
                return
            
            if not list1:
                curr.next = list2
                return helper(curr.next, list1, list2.next)
            if not list2:
                curr.next = list1
                return helper(curr.next, list1.next, list2)
            
            if list1.val < list2.val:
                curr.next = list1
                return helper(curr.next, list1.next, list2)

            else:
                curr.next = list2
                return helper(curr.next, list1, list2.next)

        helper(curr, list1, list2)
        return dummy.next