# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return True 
        def rec(lroot,rroot):
            if lroot is None and rroot is not None:
                return False 
            elif rroot is None and lroot is not None:
                return False
            elif rroot is None and lroot is None:
                return True

            if lroot.val!=rroot.val:
                return False
            else:
                return rec(lroot.left,rroot.right) and rec(lroot.right,rroot.left)
        return rec(root.left,root.right)        

        
        
