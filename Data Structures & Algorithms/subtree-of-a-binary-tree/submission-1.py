# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:return True
        if root and not subRoot:
            return False
        if not root and subRoot:
            return False
        q=deque([root])
        arr=[]
        while q:
            node=q.popleft()
            if node.val==subRoot.val:
                arr.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        def sametree(root1,root2):
            q1=deque([root1])
            q2=deque([root2])
            while q1 and q2:
                for i in range(len(q1)):
                    n1,n2=q1.popleft(),q2.popleft()
                    if not n1 and not n2:
                        continue
                    if not n1 or not n2 or n1.val!=n2.val:
                        return False
                    q1.append(n1.left)   
                    q1.append(n1.right)
                    q2.append(n2.left)
                    q2.append(n2.right)
            return True
        while arr:
            node=arr.pop()
            if sametree(node,subRoot):
                return True

        return False