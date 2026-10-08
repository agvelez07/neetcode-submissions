# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #preorder = [3,9,20,15,7] e inorder = [9,3,15,20,7]
 
        if not preorder or not inorder:
            return None
        
        # Map each inorder value to its index for O(1) lookup
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0
        
        def dfs(in_left, in_right):
            # Base case: no elements in this range
            if in_left > in_right:
                return None
            
            # Current root from preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            
            # Find root's position in inorder
            in_mid = inorder_map[root_val]
            
            # Left subtree: inorder indices [in_left, in_mid-1]
            root.left = dfs(in_left, in_mid - 1)
            # Right subtree: inorder indices [in_mid+1, in_right]
            root.right = dfs(in_mid + 1, in_right)
            
            return root
        
        return dfs(0, len(inorder) - 1)