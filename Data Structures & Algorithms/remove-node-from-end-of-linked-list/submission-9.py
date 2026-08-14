# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0

        def rec(root, head):
            nonlocal count

            if not head:
                return None
            
            head.next = rec(root, head.next)
            count += 1
            if count == n:
                return head.next
            return head

        return rec(head, head)

            