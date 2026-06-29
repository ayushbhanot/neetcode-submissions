# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        arr = []
        while curr:
            arr.append(curr)
            curr = curr.next
        
        
        for i in range(len(arr) - 1, 0, -1):
            arr[i].next = arr[i-1]
        if len(arr) > 0:
            arr[0].next = None
            return arr[-1]
        return curr

            

        #                               !
        #Curr pointing to tail 0, 1, 2, 3
        
        