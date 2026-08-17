# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        

        def rec(root, curr):

            if not curr:
                return root

            root = rec(root, curr.next)

            if root == None:
                return None

            if root == curr or root.next == curr:
                curr.next = None
                return None

            tmp = root.next

            root.next = curr

            curr.next = tmp

            return tmp

        rec(head, head) #O(n) time and space tricky recursvie solution