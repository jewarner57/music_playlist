from Node import Node


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head

    def prepend(self, data):

        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

        # if there is only 1 item set it as the tail
        if self.tail is None:
            self.tail = self.head
