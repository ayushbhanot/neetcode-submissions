# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr: #While current node exists
            temp = curr.next #Save variable we are trying to swap out
            curr.next = prev #Assign current prev instance as curr.next
            prev = curr #Reasign prev as current var before next iteration
            curr = temp #update current node as temporarily saved var
        return prev
        