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

        def rec(head):
            nonlocal nodeMap

            if not head:
                return None

            newCurr = Node(head.val)
            nodeMap[head] = newCurr
            newCurr.next = rec(head.next)
            newCurr.random = nodeMap.get(head.random, None)

            return newCurr

        return rec(head)

