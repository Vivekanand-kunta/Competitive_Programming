# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def right_most(root):
            if root!= None:
                if root.right!=None:
                    return right_most(root.right)
                else:
                    return root
            else:
                return 

        def fun(root):
            if root==None:
                return 
            if root.left==None and root.right!=None:
                root.left=root.right
                root.right=None
                fun(root.left)
            elif root.left!=None and root.right==None:
                fun(root.left)
            elif root.left!=None and root.right!=None:
                temp=right_most(root.left)
                temp.right=root.right 
                root.right=None
                fun(root.left)
            else:
                return 
        

        def right(root):
            if root!=None:
                root.right=root.left
                root.left=None 
                right(root.right)
            else:
                return
        
        fun(root)
        right(root)

        
        
