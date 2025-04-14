from Node import Node
import time

class ListAction:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node

    def traverse(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr.data.Perform()
            curr = curr.next

    def __str__(self):
        count = 0
        curr = self.head
        while curr:
            count = count + 1
            curr = curr.next
        return str(count)
