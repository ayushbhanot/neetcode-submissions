# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        curr = head

        if not self.hasKNodes(curr, k):
            return curr

        stop_node = self.getNextSeg(curr, k)
        reversed_head = self.reverseKList(curr, stop_node)
        curr.next = self.reverseKGroup(stop_node, k)
        return reversed_head

    def reverseKList(self, head, kNode): #Returns the head of reversed list
        prev, curr = None, head

        while curr != kNode:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev

    def hasKNodes(self, head, k):
        dummy = ListNode(0, head)
        curr = dummy
        count = 0
        while count < k:
            curr = curr.next
            count += 1
            if not curr:
                return False

        return True
        

    def getNextSeg(self, head, k): #Returns the head of next group
        curr = head
        while k > 0:
            curr = curr.next
            k -= 1
            if not curr:
                return None
        return curr