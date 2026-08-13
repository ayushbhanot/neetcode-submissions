# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        dummy = ListNode(0, head)
        slow, fast = head, head
        for i in range(n):
            fast = fast.next

        prev = dummy
        while slow:
            if fast == None:
                tmp = slow.next
                slow.next = None
                prev.next = tmp
                break
            prev = slow
            fast = fast.next
            slow = slow.next

        return dummy.next