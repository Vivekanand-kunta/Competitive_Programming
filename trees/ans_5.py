# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        sol=[]
        def rec(lis):
            if len(lis)==0:
                return
            temp=[]
            nodes=[]
            for ele in lis:
                if not(ele!=None):
                    return 
                temp.append(ele.val)
                if ele.left!=None:
                    nodes.append(ele.left)
                if ele.right!=None:
                    nodes.append(ele.right)
            
            sol.append(temp)
            if len(nodes)>0:
                rec(nodes)
        rec([root])
        return sol
