# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class NodeWrapper:
    def __init__(self,node:Optional[ListNode]):
        self.node=node
    def __lt__(self,other):
        return self.node.val<other.node.val
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        heap=[]
        dummy=ListNode()
        cur=dummy
        for i in lists:
            if i is not None:
                heapq.heappush(heap,NodeWrapper(i)) 
        while heap:
            nw=heapq.heappop(heap)
            cur.next=nw.node
            cur=cur.next
            if nw.node.next:
                heapq.heappush(heap,NodeWrapper(nw.node.next)) 
        return dummy.next