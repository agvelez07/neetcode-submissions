# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.min_v = root.val
        self.k = k
        def dfs(root):
            if not root:
                return
            if self.k == 0:
                return

            dfs(root.left)
            if self.k == 0:
                return
            
            self.k -= 1
            if self.k == 0:
                self.min_v = root.val
                return
                
            dfs(root.right)
           
        dfs(root)
        return self.min_v