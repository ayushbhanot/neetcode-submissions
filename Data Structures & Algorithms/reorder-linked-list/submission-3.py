# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow
        rightSeg = self.reverseList(mid.next) #O(n) time
        mid.next = None

        curr = head
        while curr and rightSeg:
            tmp = curr.next
            tmpRight = rightSeg.next

            curr.next = rightSeg
            rightSeg.next = tmp

            curr = tmp
            rightSeg = tmpRight
            

        return


    def reverseList(self, head: [ListNode]) -> [ListNode]:

        curr, prev = head, None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev