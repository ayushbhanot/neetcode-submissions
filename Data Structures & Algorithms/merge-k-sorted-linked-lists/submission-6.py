# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        while len(lists) > 1:
            nextRound = []

            for i in range(0, len(lists), 2):
                list2 = lists[i + 1] if i + 1 < len(lists) else None
                combinedList = self.helper(lists[i], list2)
                nextRound.append(combinedList)
            
            lists = nextRound

        return lists[0]

    def helper(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        curr1, curr2 = list1, list2
        dummy = ListNode(0)
        curr = dummy
        
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
        