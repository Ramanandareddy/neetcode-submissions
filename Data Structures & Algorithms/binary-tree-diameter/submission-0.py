# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        mp={None:(0,0)}
        st=[root]
        while st:
            node=st[-1]
            if node.left and node.left not in mp:
                st.append(node.left)
            elif node.right and node.right not in mp:
                st.append(node.right)
            else:
                node=st.pop()
                leftheight,leftdia=mp[node.left]
                rightheight,rightdia=mp[node.right]
                mp[node]=(1+max(leftheight,rightheight),max(leftheight+rightheight,leftdia,rightdia))
        return mp[root][1]
                