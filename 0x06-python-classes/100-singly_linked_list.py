#!/usr/bin/python3
"""100-singly_linked_list modules contains a Node class that defines a node
    of a singly linked list.

    SinglyLinkedList class that defines a singly linked list.
"""


class Node:
    """Node class defines a node of a singly linked list
    """
    def __init__(self, data, next_node=None):
        """Initialize the class attribute

        Args:
            data(:obj:`int`): The data part of the node
            next_node(:obj:`Node`): The address of the next node
        """
        if type(data) != int:
            print("data must be an integer", end="")
            raise TypeError
        else:
            self.__data = data

        if next_node is not None and type(next_node) != Node:
            print("next_node must be a Node object", end="")
            raise TypeError
        else:
            self.__next_node = next_node

    @property
    def data(self):
        """Retrieve the data part of the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data part of the node

        Args:
            value(:obj:`int`): The data to be set
        """
        if type(value) != int:
            print("data must be an integer", end="")
            raise TypeError
        else:
            self.__data = value

    @property
    def next_node(self):
        """Retrieve the address of the next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the address of the next node

        Args:
            value(:obj:`Node`): The address of the next node
        """
        if value is not None and type(value) != Node:
            print("next_node must be a Node object", end="")
            raise TypeError
        else:
            self.__next_node = value


class SinglyLinkedList:
    """SinglyLinkedList class defines a singly linked list
    """
    def __init__(self):
        """Initializes the instance attribute
        """
        self.__head = None

    def __str__(self):
        """Print the entire list in stdout, one node number by line
        """
        current = self.__head
        output = ""
        while current is not None:
            # print(current.data)
            output += "{}".format(current.data)
            current = current.next_node
            if current is not None:
                output += '\n'
        return output

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in
            the list(increasing order)

        Args:
            value(:obj:`int`): The data to be inserted
        """
        new_node = Node(value)
        if self.__head is None:
            new_node = Node(value)
            self.__head = new_node
        else:
            temp = self.__head
            while temp is not None:
                if value < temp.data and temp == self.__head:
                    new_node.next_node = self.__head
                    self.__head = new_node
                    break
                elif value < temp.data:
                    new_node.next_node = temp
                    prev.next_node = new_node
                    break
                elif value >= temp.data and not temp.next_node:
                    temp.next_node = new_node
                    break
                else:
                    prev = temp
                    temp = temp.next_node
