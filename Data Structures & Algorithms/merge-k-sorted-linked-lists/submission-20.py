from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        q = deque()

        if not lists:
            return None

        for _list in lists:
            q.append(_list)

        while len(q) > 1:
            list1 = q.popleft()
            list2 = q.popleft()
            q.append(self.mergeSortedLists(list1, list2))

        return q.popleft()
        
    def mergeSortedLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> ListNode:

        if not list1 and not list2:
            return None

        if not list1:
            return list2

        if not list2:
            return list1

        dummy = ListNode(0)
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next

            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        if list1:
            curr.next = list1

        elif list2:
            curr.next = list2

        return dummy.next