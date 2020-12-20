# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        item_num = len(preorder)
        if item_num == 0:
            return None
        elif item_num == 1:
            return TreeNode(preorder[0])
        else:
            root_value = preorder[0]
            root = TreeNode(root_value)
            inorder_root_index = inorder.index(root_value)
            root.left = self.buildTree(preorder[1:1 + inorder_root_index], inorder[:inorder_root_index])
            root.right = self.buildTree(preorder[1 + inorder_root_index:], inorder[1 + inorder_root_index:])
            return root