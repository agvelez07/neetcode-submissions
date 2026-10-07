# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return [True, 0]
        
            left_side  = dfs(root.left)
            right_side = dfs(root.right)
            balanced = False
            if left_side[0] and right_side[0] and abs(left_side[1] - right_side[1]) <= 1:
                balanced = True
            
            return [balanced, 1 + max(left_side[1], right_side[1])]

        return dfs(root)[0]