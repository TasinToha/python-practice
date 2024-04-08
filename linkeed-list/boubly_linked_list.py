# Description: This file contains the implementation of a doubly linked list
# Node class
class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return repr(self.data)
    

# Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = Node()


    def __repr__(self):
        nodes = []
        current_node = self.head.next

        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node.next

        return ", ".join(nodes)


    def append(self, data):
        node = Node(data)

        if self.head.next is None:
            self.head.next = node

            return
        
        current_node = self.head.next
        while current_node.next:
            current_node = current_node.next

        current_node.next = node
        node.prev = current_node


    def prepend(self, data):
        first_node = self.head.next
        new_node = Node(data, None, first_node)
        self.head.next = new_node

        if first_node:
            first_node.prev = new_node


    def search(self, item):
        current_node = self.head.next

        while current_node:
            if current_node.data == item:
                return current_node

            current_node = current_node.next

        return None


    def remove(self, data):
        current_node = self.head

        while current_node:
            if current_node.data == data:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next
                
                if current_node.next:
                    current_node.next.prev = current_node.prev
                else:
                    self.tail = current_node.prev

                break

            current_node = current_node.next


    def insert(self, data, new_data):
        current_node = self.head

        while current_node:
            if current_node.data == data:
                new_node = Node(new_data, current_node, current_node.next)
                current_node.next = new_node
                new_node.next.prev = new_node
                break

            current_node = current_node.next