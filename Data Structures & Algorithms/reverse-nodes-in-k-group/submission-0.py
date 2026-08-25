# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        curr = head
        newHead = self.getKNode(curr, k)
        if not newHead:
            return head

        prevTail = None

        while curr:
            segHead = self.getKNode(curr, k) # Head of reversed seg
            if not segHead:
                break
            nextHead = segHead.next # Head of next segment
            if prevTail:
                prevTail.next = segHead
            prevTail = self.reverseKthList(curr, segHead) # Tail of reversed seg
            prevTail.next = nextHead
            curr = nextHead

        return newHead

    def reverseKthList(self, head, kNode): #returns tail
        
        prev, curr = None, head

        newSegment = kNode.next

        while curr != newSegment:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return head

    def getKNode(self, head, k): #returns head and if it is reversible
        k -= 1
        curr = head

        while k > 0:
            if not curr:
                return None
            curr = curr.next
            k -= 1

        return curr

        