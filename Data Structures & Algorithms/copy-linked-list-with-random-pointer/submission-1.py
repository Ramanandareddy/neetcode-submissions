"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        otc={None:None}
        cur=head
        while cur:
            otc[cur]=Node(cur.val)
            cur=cur.next
        cur=head
        while cur:
            cop=otc[cur]
            cop.next=otc[cur.next]
            cop.random=otc[cur.random]
            cur=cur.next
        return otc[head]