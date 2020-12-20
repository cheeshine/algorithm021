# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root is p or root is q:
            return root

        left_ret = self.lowestCommonAncestor(root.left, p, q)
        right_ret = self.lowestCommonAncestor(root.right, p, q)

        if left_ret is None:
            return right_ret
        if right_ret is None:
            return left_ret

        return root
