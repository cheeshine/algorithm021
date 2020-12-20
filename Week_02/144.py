# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            ret = [root.val]
            ret.extend(self.preorderTraversal(root.left))
            ret.extend(self.preorderTraversal(root.right))
            return ret
        return []