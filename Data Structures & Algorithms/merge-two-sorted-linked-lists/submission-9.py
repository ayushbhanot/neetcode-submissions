# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0, None)

        def helper(curr, list1, list2):
            if not list1:
                curr.next = list2
                return
            elif not list2:
                curr.next = list1
                return

            if list1.val < list2.val:
                curr.next = list1
                return helper(list1, list1.next, list2)
            elif list2.val <= list1.val:
                curr.next = list2
                return helper(list2, list1, list2.next)

        helper(dummy, list1, list2)

        return dummy.next #O(n + m) time and space Top-Down Recursive Solution
                