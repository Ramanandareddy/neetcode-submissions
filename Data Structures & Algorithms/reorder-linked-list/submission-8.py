# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast=head.next
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        prev=None
        curr=slow.next
        slow.next=None
        while curr:
            tmp=curr.next
            curr.next=prev
            prev=curr
            curr=tmp
        f=head
        s=prev
        while s:
            t1=f.next
            t2=s.next
            f.next=s
            s.next=t1
            f=t1
            s=t2
