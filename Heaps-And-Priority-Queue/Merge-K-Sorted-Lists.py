# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        heapq.heapify(heap)

        for root in lists:
            while root:
                heapq.heappush(heap,(root.val, id(root), root))
                root = root.next

        root, ptr = None, None
        while heap:

            val,ID,node = heapq.heappop(heap)
            if root is None:
                root = ptr = node

            else:
                ptr.next = node
                ptr = ptr.next

        if ptr:
            ptr.next = None
        return root
