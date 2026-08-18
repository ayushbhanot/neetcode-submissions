# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        curr = dummy
        carry = False
        while l1 or l2 or carry:
            val = 0
            if carry == True:
                val += 1
            carry = False
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            if val >= 10:
                val = val % 10
                carry = True
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next