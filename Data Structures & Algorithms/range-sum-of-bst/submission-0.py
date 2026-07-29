# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res=0
        q=deque([root])
        while q:
            node=q.popleft()
            if node and low<=node.val<=high:
                res+=node.val
                q.append(node.left)
                q.append(node.right)
            if node and node.val<low:
                q.append(node.right)
            if node and node.val>high:
                q.append(node.left)
        return res
