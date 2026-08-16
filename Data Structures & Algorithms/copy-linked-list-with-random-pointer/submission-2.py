"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        nodeMap = {}

        if not head:
            return None
            
        curr = head
        while curr:
            nodeMap[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr.next:
            nodeMap[curr].next = nodeMap[curr.next]
            curr = curr.next

        curr = head
        while curr:
            if curr.random != None:
                nodeMap[curr].random = nodeMap[curr.random]
            else:
                nodeMap[curr].random = None
            curr = curr.next

        return nodeMap[head]
        