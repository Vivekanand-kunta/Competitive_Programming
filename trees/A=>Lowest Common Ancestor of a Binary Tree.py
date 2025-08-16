# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        sol=[]
        def self_checker(root,q):
            if root is None:
                return False
            else:
                if root==q:
                    return True
                else:
                    return self_checker(root.left,q) or self_checker(root.right,q)
        
        def checker(root):
            if root is None:
                return False
            else:
                if root==p:
                    if self_checker(root,q):
                        sol.append(p)
                    return True
                elif root==q:
                    if self_checker(root,p):
                        sol.append(q)
                    return True
                else:
                    left=checker(root.left)
                    right=checker(root.right)
                    if left and right:
                        sol.append(root)
                        return True
                    else:
                        return left or right
        checker(root)
        return sol[0] 


        
