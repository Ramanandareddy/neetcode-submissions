# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        gp=dummy
        def getkth(cur,k):
            while cur and k:
                cur=cur.next
                k-=1
            return cur
        while True:
            kth=getkth(gp,k)
            if not kth:
                break
            gn=kth.next
            prev,cur=gn,gp.next
            while cur!=gn:
                tmp=cur.next
                cur.next=prev
                prev=cur
                cur=tmp
            tmp=gp.next
            gp.next=kth
            gp=tmp
        return dummy.next
            
