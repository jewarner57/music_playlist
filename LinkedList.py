from Node import Node


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head

    def prepend(self, data):
        """Add an item to the beginning of the list"""

        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

        # if only one node, set it to tail
        if self.tail is None:
            self.tail = self.head

    def append(self, data):
        """Add an item to the end of the list"""

        newNode = Node(data)

        if self.tail is not None:
            self.tail.next = newNode

        self.tail = newNode

        # if only one node set it to head
        if self.head is None:
            self.head = newNode

    def printList(self):
        node = self.head

        while node is not None:
            print(node.data)
            node = node.next
