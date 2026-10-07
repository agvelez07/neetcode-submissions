# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        inorder = []
        if root.left:
            inorder += self.inorderTraversal(root.left)
        inorder.append(root.val)
        if root.right:
            inorder += self.inorderTraversal(root.right)

        return inorder