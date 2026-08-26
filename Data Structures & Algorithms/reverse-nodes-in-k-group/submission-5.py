# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        curr = head
        dummy = ListNode(0, head)
        prev_tail = dummy
        while curr:
            if not self.hasCount(curr, k):
                prev_tail.next = curr
                break
            next_head = self.getNextSeg(curr, k)
            reversed_head, reversed_tail = self.reverseKList(curr, next_head)
            if prev_tail:
                prev_tail.next = reversed_head
            prev_tail = reversed_tail
            reversed_tail.next = next_head
            curr = next_head
        
        return dummy.next
            
    def hasCount(self, head, k):
        curr = head
        k -= 1
        while k > 0:
            curr = curr.next
            k -= 1
            if not curr:
                return False
        return True

    def reverseKList(self, head, kNode): #O(k) time O(1) space returns tail of reversed head
        prev, curr = None, head
        while curr != kNode:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev, head

    def getNextSeg(self, head, k): #O(k) time O(1) space returns tail, head of next segment
        curr = head
        while k > 0:
            if not curr:
                return None
            curr = curr.next
            k -= 1
        return curr
        