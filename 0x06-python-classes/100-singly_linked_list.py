#!/usr/bin/python3
"""this module defines a class Square"""


class Node:
    """Represents a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initializes the Node instance"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the value of the data attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the value of the data attribute"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the value of the next_node attribute"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the value of the next_node attribute"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list"""

    def __init__(self):
        """Initializes the SinglyLinkedList instance"""
        self.head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct
        sorted position in the list (increasing order)"""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and value > current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Prints the entire list in stdout, one node number by line"""
        if self.head is None:
            return ""
        current = self.head
        node_list = []
        while current:
            node_list.append(str(current.data))
            current = current.next_node
        return "\n".join(node_list)
