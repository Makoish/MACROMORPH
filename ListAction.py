from Node import Node
import time

class ListAction:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def traverse(self):
        curr = self.head
        while curr:
            curr.data.Perform()
            curr = curr.next
