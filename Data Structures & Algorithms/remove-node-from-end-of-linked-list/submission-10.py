# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        slow, fast = head, head

        for i in range(n):
            fast = fast.next
        
        dummy = ListNode(0, head)
        prev = dummy
        while slow:
            if fast == None:
                prev.next = slow.next
                break
            prev = slow
            slow = slow.next
            fast = fast.next
        
        return dummy.next #O(n) time and O(1) space best solution