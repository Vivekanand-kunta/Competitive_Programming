# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        sol=[0,-float('inf')]
        def rec(root):
            if root==None:
                return 0
            left=rec(root.left)
            right=rec(root.right)
            sol[0]=max(sol[0],left+right+root.val)
            sol[1]=max(sol[1],root.val)
            return max((max(left,right)+root.val),0)
        rec(root)

        if sol[0]==0:
            return sol[1]
        return sol[0] 
            


        
