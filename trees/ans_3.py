# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def rec(root):
            if root==None:
                return [0,True]
            else:
                left,c1=rec(root.left)
                right,c2=rec(root.right)

                if not (c1 and c2):
                    return [0,False]
                if abs(left-right)>1:
                    return [0,False]
                else:
                    return [1+max(left,right),True]
        return rec(root)[1]
        
