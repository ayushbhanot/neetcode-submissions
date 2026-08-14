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
            nodes.append(curr)
            curr = curr.next
        
        removalIndex = len(nodes) - n

        if removalIndex == 0:
            return nodes[removalIndex].next

        nodes[removalIndex - 1].next = nodes[removalIndex].next
        nodes[removalIndex].next = None

        return head