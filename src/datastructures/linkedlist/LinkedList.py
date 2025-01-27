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
    
    def size(self):
        count = 0
        if self.head == None:
            return count
        currentNode = self.head
        while currentNode:
            count += 1
            currentNode = currentNode.next
        return count

    def prepend(self, value):
        node = LinkedListNode(value, self.head)
        self.head = node
    
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

    def deleteHead(self):
        if not self.head:
            return None
        deletedHead = self.head
        if self.head.next:
            self.head = self.head.next
        else:
            self.head = None
            self.tail = None
        return deletedHead

    def search(self, value):
        node = None
        if self.head == None:
            return node
        for item in self:
            if item.value == value:
                node = item
        return node

    def reverse(self):
        previous = None
        current = self.head
        following = current.next
        while current:
            current.next = previous
            previous = current
            current = following
            if following:
                following = following.next
        self.head = previous
