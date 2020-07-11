from src.datastructures.linkedlist.LinkedListNode import LinkedListNode

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    def append(self, value):
        node = LinkedListNode(value)
        if self.head == None:
            self.head = node
            self.tail = node
            return self
        self.tail.next = node
        self.tail = node
        return self
    
    def remove(self, value):
        if not self.head:
            return None
        if self.head.value == value:
            self.head = self.head.next
            return self
        prevNode = self.head
        for node in self:
            if node.value == value:
                prevNode.next = node.next
                if node.next == None:
                    self.tail = prevNode
                return self
            prevNode = node
