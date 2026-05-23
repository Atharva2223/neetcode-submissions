# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def solve(self,node,p,q) -> TreeNode:

        if node is None:
            return None
        if node.val == p.val or node.val == q.val:
            return node
        left = self.solve(node.left,p,q)
        right = self.solve(node.right,p,q)

        if left is None and right is None :
            return None
        elif left is None:
            return right
        elif right is None:
            return left
        return node
    
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        x = self.solve(root,p,q)    
        return x