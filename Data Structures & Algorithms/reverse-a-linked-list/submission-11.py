# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None

        def helper(curr, prev):

            if not curr:
                return prev
            tmp = curr.next

            curr.next = prev

            return helper(tmp, curr)

        return helper(head, None)