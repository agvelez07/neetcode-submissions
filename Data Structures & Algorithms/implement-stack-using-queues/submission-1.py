class Node:
    def __init__(self, val = -1):
        self.val = val
        self.next = None
class MyStack:
    def __init__(self):
        self.head = None

    def push(self, x: int) -> None:
        new_node = Node(x)
        if self.head:
            new_node.next = self.head
            self.head = new_node
            return
        self.head = new_node

    def pop(self) -> int:
        if not self.head: 
            return
        temp = self.head
        if self.head.next:
            self.head = self.head.next
        else:
            self.head = None
        return temp.val

    def top(self) -> int:
        return self.head.val
        
    def empty(self) -> bool:
        if self.head:
            return False
        return True



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()