# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q=deque()
        h=0
        mh=0
        q.append([root,h])
        res=[]
        ch={}
        while q:
            node,h=q.popleft()
            ch[h]=node.val
            if node.left:
                q.append([node.left,h+1])
            if node.right:
                q.append([node.right,h+1])
        print(ch)
        for i in ch.values():
            res.append(i)

        return res