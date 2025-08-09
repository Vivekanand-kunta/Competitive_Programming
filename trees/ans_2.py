# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        var=[-float('inf')]

        def rec(root):
            if root !=None:
                left_height=rec(root.left)
                right_height=rec(root.right)
                var[0]=max(var[0],1+left_height+right_height)
                return 1+max(left_height,right_height)
            else:
                return 0
        rec(root)
        return var[0]-1
