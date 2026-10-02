class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:

    def __init__(self):
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0 and cur != self.right:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        next = self.left.next

        new_node.prev = self.left
        new_node.next = next

        next.prev = new_node
        self.left.next = new_node
        return

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        prev = self.right.prev

        new_node.next = self.right
        new_node.prev = prev

        self.right.prev = new_node
        prev.next = new_node
        return

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0:
            new_node = Node(val)

            new_node.next = cur
            new_node.prev = cur.prev

            cur.prev.next = new_node
            cur.prev = new_node
        return

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0 and cur != self.right:
            prev_node = cur.prev
            next_node = cur.next
            prev_node.next = next_node
            next_node.prev = prev_node
         
        return

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)