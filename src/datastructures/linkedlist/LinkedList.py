from src.datastructures.linkedlist.LinkedListNode import LinkedListNode

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, value):
        node = LinkedListNode(value)
        if self.head == None:
            self.head = node
            self.tail = node
            return self
        self.tail.next = node
        self.tail = node
        return self
            