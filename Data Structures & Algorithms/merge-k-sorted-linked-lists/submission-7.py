import heapq

class NodeWrapper:
    def __init__(self, node: ListNode):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        _lists = len(lists)

        heap = []
        dummy = ListNode(0)
        curr = dummy

        for _list in lists:
            if not _list:
                continue
            heapq.heappush(heap, NodeWrapper(_list))

        while heap:
            node_wrapper = heapq.heappop(heap)
            curr.next = node_wrapper.node
            curr = curr.next
            
            if node_wrapper.node.next:
                heapq.heappush(heap, NodeWrapper(node_wrapper.node.next))


        return dummy.next

