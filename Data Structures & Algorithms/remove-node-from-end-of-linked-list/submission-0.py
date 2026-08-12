# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        reversedHead = self.reverse(head)
        
        count = 0
        dummy = ListNode(0, reversedHead)
        curr, prev = dummy, dummy

        while curr:
            if count == n:
                tmp = curr.next
                curr.next = None
                prev.next = tmp

            prev = curr
            curr = curr.next
            count += 1

        return self.reverse(dummy.next)



    def reverse(self, head: [ListNode]) -> [ListNode]:

        if not head:
            return None
        
        curr, prev = head, None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev
