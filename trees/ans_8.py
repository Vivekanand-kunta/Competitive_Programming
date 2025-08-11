# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        sol=[]
        def check(root,node):
            if root==None:
                return False
            if root==node:
                return True 
            
            return check(root.left,node) or check(root.right,node)
        
        def rec(root):
            if root==None:
                return False 
            if root==p:
                if check(root,q):
                    if len(sol)==0:
                        sol.append(root)
                    return True 
                else:
                    return True
            if root==q:
                if check(root,p):
                    if len(sol)==0:
                        sol.append(root)
                    return True 
                else:
                    return True
            left=rec(root.left)
            right=rec(root.right)

            if left and right:
                if len(sol)==0:
                        sol.append(root) 
            return left or right
        rec(root)
        return sol[0]
            


            



        
