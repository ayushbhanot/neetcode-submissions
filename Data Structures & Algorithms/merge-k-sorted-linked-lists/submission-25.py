import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node
        self.val = node.val

    def __lt__(self, other):
        return self.val < other.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None
        
        heap = []

        for _list in lists: #O(k) time
            if not _list:
                continue
            heapq.heappush(heap, NodeWrapper(_list))

        dummy = ListNode(0)
        curr = dummy

        while len(heap) > 0:
            popped = heapq.heappop(heap).node
            curr.next = popped
            curr = curr.next
            if popped.next:
                heapq.heappush(heap, NodeWrapper(popped.next))
        
        return dummy.next
