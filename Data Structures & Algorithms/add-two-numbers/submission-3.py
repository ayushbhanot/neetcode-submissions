# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while curr:
            val = 0
            val += carry
            if not l1 and not l2 and carry == 0:
                curr.next = None
                break
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            if val >= 10:
                carry = 1
                val = val % 10
            else:
                carry = 0

            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next