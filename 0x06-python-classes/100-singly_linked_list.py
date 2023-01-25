#!/usr/bin/python3

"""class of a singly-linked list."""


class Node:
    """node in a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initializes a new node

        Args:
            data(int): data of the Node
            next_node (Node): next node of the Node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A singly linked list"""
    def __init__(self):
        """A new SinglyLinkedList"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node to the SinglyLinkedList in the correct order

        Args:
            value(Node): the new Node to insert
        """
        lists = Node(value)
        if self.__head is None:
            lists.next_node = None
            self.__head = lists
        elif self.__head.data > value:
            lists.next_node = self.__head
            self.__head = lists
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            lists.next_node = tmp.next_node
            tmp.next_node = lists

    def __str__(self):
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ("\n".join(values))
