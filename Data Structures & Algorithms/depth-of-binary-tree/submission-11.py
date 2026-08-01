# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        st=[(root,1)]
        res=0
        while st:
            node,dep=st.pop()
            if node.left:
                st.append((node.left,dep+1))
            if node.right:
                st.append((node.right,dep+1))
            res=max(res,dep)
        return res

