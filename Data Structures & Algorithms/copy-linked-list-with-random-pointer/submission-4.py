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
        
        if not head:
            return None

        curr = head
        while curr:
            copyNode = Node(curr.val)
            tmp = curr.next
            curr.next = copyNode
            copyNode.next = tmp
            curr = tmp

        l1 = head

        while l1:
            if l1.random:
                l2 = l1.next
                random = l1.random
                l2.random = random.next
            l1 = l1.next.next

        

        l1 = head
        newHead = l1.next
        while l1:
            l2 = l1.next
            l1.next = l1.next.next
            l1 = l1.next
            if l1 and l1.next:
                l2.next = l1.next
            else:
                l2.next = None

        return newHead