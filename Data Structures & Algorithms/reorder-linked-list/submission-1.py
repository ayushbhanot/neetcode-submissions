# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        nodes = []

        curr = head
        while curr: #O(n) time
            nodes.append(curr) #O(n) space
            curr = curr.next
        
        l, r = 0, len(nodes) - 1
        while l < r:
            tmp = nodes[l].next
            nodes[l].next = nodes[r]
            nodes[r].next = tmp
            l += 1
            r -= 1

        if nodes and l < len(nodes):
            nodes[l].next = None
        return #O(n) time and space!