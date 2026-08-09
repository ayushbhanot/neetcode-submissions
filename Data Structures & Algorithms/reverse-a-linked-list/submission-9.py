# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr, prev = head, None

        while curr: #O(n) time and O(n) space
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev
