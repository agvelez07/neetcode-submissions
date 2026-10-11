from typing import List

class TreeNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self.root = None

    def _insert(self, curr_node, new_node):
        if curr_node is None:
            return new_node
        
        if new_node.key < curr_node.key:
            curr_node.left = self._insert(curr_node.left, new_node)
        elif new_node.key > curr_node.key:
            curr_node.right = self._insert(curr_node.right, new_node)
        else:
            curr_node.val = new_node.val
        
        return curr_node

    def insert(self, key: int, val: int) -> None:
        if key is None or val is None:
            return

        new_node = TreeNode(key, val)
        self.root = self._insert(self.root, new_node)

    def get(self, key: int) -> int:
        if self.root is None:
            return -1

        cur = self.root
        while cur:
            if cur.key == key:
                return cur.val
            elif key < cur.key:
                cur = cur.left
            else: 
                cur = cur.right
        return -1 

    def getMin(self) -> int:
        if self.root is None:
            return -1

        cur = self.root
        while cur and cur.left:
            cur = cur.left
        return cur.val

    def getMax(self) -> int:
        if self.root is None:
            return -1

        cur = self.root
        while cur and cur.right:
            cur = cur.right
        return cur.val

    def remove(self, key: int) -> None:
        if key is None:
            return
        self.root = self._remove(self.root, key)

    def _remove(self, cur, key: int):
        if cur is None:
            return None

        if key < cur.key:
            cur.left = self._remove(cur.left, key)
        elif key > cur.key:
            cur.right = self._remove(cur.right, key)
        else:
            if cur.left is None:
                return cur.right
            elif cur.right is None:
                return cur.left
            
            min_node = cur.right
            while min_node.left:
                min_node = min_node.left
            
            cur.key = min_node.key
            cur.val = min_node.val
            cur.right = self._remove(cur.right, min_node.key)
            
        return cur

    def getInorderKeys(self) -> List[int]:
        inorder = []
        
        def dfs(cur):
            if cur is None:
                return
            dfs(cur.left)
            inorder.append(cur.key)
            dfs(cur.right)
        
        dfs(self.root)
        return inorder