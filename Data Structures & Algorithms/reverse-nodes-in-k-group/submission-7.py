# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head

        if not self.getStopNode(curr, k):
            return curr
        stop_node = self.getStopNode(curr, k)
        next_head = stop_node.next
        reversed_head, reversed_tail = self.reverseKList(curr, next_head)
        reversed_tail.next = self.reverseKGroup(next_head, k)
        return reversed_head

        
    def getStopNode(self, head, k):
        curr = head
        k -= 1
        while k > 0:
            if not curr:
                return None
            curr = curr.next
            k -= 1
        return curr
        
    def reverseKList(self, head, next_head):
        prev, curr = None, head
        while curr != next_head:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev, head