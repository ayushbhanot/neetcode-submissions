# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None

        return self.divideLists(0, len(lists) - 1, lists)

    def divideLists(self, l, r, lists):
        if l == r:
            return lists[r]

        m = l + (r - l) // 2

        left = self.divideLists(l, m, lists)
        right = self.divideLists(m + 1, r, lists)

        return self.mergeLists(left, right)

    def mergeLists(self, list1, list2):

        if not list1 and not list2:
            return None

        if not list1:
            return list2

        elif not list2:
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