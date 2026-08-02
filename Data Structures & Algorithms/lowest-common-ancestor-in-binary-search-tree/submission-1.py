# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        qu=deque([root])
        res=None

        low = min(p.val, q.val)
        high = max(p.val, q.val)
        while qu:
            node=qu.popleft()
            if low<=node.val<=high:
                res=node
                break
            if node.left:
                qu.append(node.left)
            if node.right:
                qu.append(node.right)

        return res