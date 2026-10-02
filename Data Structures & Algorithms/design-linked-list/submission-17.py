class Node:
    def __init__(self, val=0, next=None , prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        if self.size == 0:
            return -1
        node = self.head
        for _ in range(index):
            node = node.next
        return node.val

    def get_node(self, index: int):
        if index < 0 or index >= self.size:
            return None
        if self.size == 0:
            return None
        node = self.head
        for _ in range(index):
            node = node.next
        return node

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return

        temp = self.head
        print('a', temp.val)
        self.head = new_node
        print('b', temp.val)
        self.head.next = temp
        print('c', temp.val)
        temp.prev = self.head
        print('d', temp.val)
        self.size += 1
        return

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.size == 0:
          return  self.addAtHead(val)

        temp = self.tail
        self.tail = new_node
        self.tail.prev = temp

        temp.next = self.tail
        self.size += 1
        return

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
           return self.addAtHead(val)
        if index == self.size:
            return self.addAtTail(val)

        new_node = Node(val)
        curr = self.get_node(index)
        prev_node = curr.prev

        new_node.prev = prev_node
        new_node.next = curr
        prev_node.next = new_node
        curr.prev = new_node
        self.size += 1 
        return

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        elif self.size < 2:
            self.head = None
            self.tail = None
            self.size = 0
            return

        node_to_delete = self.get_node(index)

        if node_to_delete == self.head:
            self.head = node_to_delete.next
            self.head.prev = None
        elif node_to_delete == self.tail:
            self.tail = node_to_delete.prev
            self.tail.next = None
        else:
            next_node = node_to_delete.next
            prev_node = node_to_delete.prev

            next_node.prev = prev_node
            prev_node.next = next_node
        self.size -= 1

        return
 
# Your MyLinkedList object will be instantiated and called as such:
#obj = MyLinkedList()
#param_1 = obj.get(index)
#obj.addAtHead(val)
#obj.addAtTail(val)
#obj.addAtIndex(index,val)
#obj.deleteAtIndex(index)