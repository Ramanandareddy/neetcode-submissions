# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return None
        q=deque([(root,root.val)])
        res=0
        while q:
            node,mv=q.popleft()
            if node.val>=mv:                          
                res+=1
                mv=max(mv,node.val)
            if node.left:
                q.append((node.left,max(node.left.val,mv)))
            if node.right:
                q.append((node.right,max(node.right.val,mv)))
        return res


