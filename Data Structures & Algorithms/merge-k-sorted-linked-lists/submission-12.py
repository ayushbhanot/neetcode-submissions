# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        numberOfLists = len(lists)

        while numberOfLists > 1:
            nextRound = []
            for i in range(0, len(lists), 2):
                list2 = lists[i + 1] if i + 1 < len(lists) else []
                nextRound.append(self.mergeLists(lists[i], list2))
            lists = nextRound
            numberOfLists = len(nextRound)

        return lists[0]

        

    def mergeLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        if not list1 and not list2:
            return None
        
        if not list1:
            return list2
        if not list2:
            return list1

        dummy = ListNode(0)
        curr = dummy

        curr1, curr2 = list1, list2

        while curr1 and curr2:
            if curr1.val < curr2.val:
                curr.next = curr1
                curr1 = curr1.next

            else:
                curr.next = curr2
                curr2 = curr2.next

            curr = curr.next

        if curr1:
            curr.next = curr1
        elif curr2:
            curr.next = curr2

        return dummy.next
        