# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        nodes = []
        curr = head

        while curr:
            nodes.append(curr) #O(n) space
            curr = curr.next #O(n) time

        removedNode = nodes[len(nodes) - n]

        dummy = ListNode(0, head)
        curr, prev = head, dummy

        while curr:
            if curr == removedNode:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next

        return dummy.next

        