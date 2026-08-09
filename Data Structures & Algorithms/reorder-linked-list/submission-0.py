# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow
        rightSeg = self.reverseList(mid.next)
        mid.next = None

        curr = head
        while curr and rightSeg:
            tmp = curr.next
            curr.next = rightSeg
            tmpmid = rightSeg.next
            rightSeg.next = tmp
            rightSeg = tmpmid
            curr = tmp

        return


    def reverseList(self, head: [ListNode]) -> [ListNode]:
        if not head:
            return None

        curr, prev = head, None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev