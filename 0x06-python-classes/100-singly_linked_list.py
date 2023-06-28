#!/usr/bin/python3
"""Defines a node of a singly linked list."""

class Node:
    """
    This class represents a node of a singly linked list.

    Attributes:
        __data (int): The data stored in the node.
        __next_node (Node): The next node in the linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the Node class.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node): The next node in the linked list. Defaults to None.

        Raises:
            TypeError: If data is not an integer or next_node is not None or a Node object.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method to retrieve the data stored in the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method to set the data stored in the node.

        Args:
            value (int): The data to be stored in the node.

        Raises:
            TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Getter method to retrieve the next node in the linked list.

        Returns:
            Node: The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method to set the next node in the linked list.

        Args:
            value (Node): The next node in the linked list.

        Raises:
            TypeError: If next_node is not None or a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be None or a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    This class represents a singly linked list.

    Attributes:
        head: The first node in the linked list.
    """

    def __init__(self):
        """
        Initializes a new instance of the SinglyLinkedList class.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).

        Args:
            value (int): The value of the new Node to be inserted.
        """
        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and value >= current.next_node.data:
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        current = self.head
        nodes = []
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)
