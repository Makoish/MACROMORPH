from Node import Node
import pickle
from Delay import Delay
import threading

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

    def load_from_pickel_file(self, file_path):
        with open(file_path, 'rb') as f:
            loaded_list = pickle.load(f)
        
        for act in loaded_list:
            self.append(act)

        

    def traverse(self, delay):
        curr = self.head
        while curr:
            if isinstance(curr.data, Delay) and not delay:
                curr = curr.next
                continue

            curr.data.Perform()
            curr = curr.next
            



    @staticmethod
    def load(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)
