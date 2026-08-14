# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        N = 0
        while curr:
            N += 1
            curr = curr.next

        removalNode = N - n + 1 #1, 2, 3, 4

        if removalNode == 1:
            return head.next

        curr, prev = head, None
        count = 0
        while curr:
            count += 1
            if count == removalNode:
                prev.next = curr.next
                curr.next = None
            prev = curr
            curr = curr.next

        return head