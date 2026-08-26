# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        new_head = curr
        prev_tail = None
        while curr:
            if not self.getCurrTail(curr, k):
                prev_tail.next = curr
                break
            next_head = self.getCurrTail(curr, k).next
            reversed_head, reversed_tail = self.reverseKList(curr, k)
            if prev_tail:
                prev_tail.next = reversed_head
            elif not prev_tail:
                new_head = reversed_head
            prev_tail = curr
            reversed_tail.next = next_head
            curr = next_head

        return new_head

        
    def getCurrTail(self, head, k): #O(k) time and O(1) space returns current segment tail
        curr = head
        count = 1
        while count < k:
            if not curr:
                return None
            curr = curr.next
            count += 1

        return curr

    def reverseKList(self, head, k): #O(k) time and O(1) space returns reversed head and tail
        prev = None
        curr = head
        count = 0
        while count < k:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            count += 1
        
        return (prev, head)
        
