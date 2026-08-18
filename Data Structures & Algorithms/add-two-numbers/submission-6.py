# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def rec(l1, l2, carry):

            if not l1 and not l2 and not carry:
                return None
                
            val = 0
            val += carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            
            carry = val // 10
            val = val % 10

            newNode = ListNode(val)
            newNode.next = rec(l1, l2, carry)

            return newNode

        return rec(l1, l2, 0)