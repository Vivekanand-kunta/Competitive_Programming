# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def rec(root,count):
            if root!= None:
                left=1+rec(root.left,0)
                right=1+rec(root.right,0)
                return max(left,right)
            else:
                return 0
        return rec(root,0)
