import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Node_Wrapper:
    def __init__(self, node: ListNode):
        self.node = node
        self.val = self.node.val
        self.next = self.node.next

    def __lt__(self, other):
        return self.val < other.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        dummy = ListNode(0)
        curr = dummy

        for _list in lists:
            if _list:
                heapq.heappush(heap, Node_Wrapper(_list))

        while len(heap) > 0:
            minNode = heapq.heappop(heap).node
            curr.next = minNode
            curr = curr.next
            if minNode.next:
                heapq.heappush(heap, Node_Wrapper(minNode.next))

        return dummy.next